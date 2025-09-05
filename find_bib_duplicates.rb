#!/usr/bin/env ruby
# Script to find duplicate entries in a BibTeX file based on title and DOI.


def normalize_title(title)
  title.downcase
       .gsub(/[{}]/, '')
       .gsub(/[^a-z0-9\s]/, '')
       .gsub(/\s+/, ' ')
       .strip
end

if ARGV.empty?
  puts "Uso: ruby #{__FILE__} file.bib"
  exit 1
end

bibfile = ARGV[0]
unless File.exist?(bibfile)
  puts "File #{bibfile} non trovato!"
  exit 1
end

title_index = {}
doi_index = {}
duplicates = []

current_entry = nil
current_title = nil
current_doi = nil

File.foreach(bibfile) do |line|
  if line.strip.start_with?('@')
    unless current_entry.nil?
      if current_title
        if title_index.key?(current_title)
          duplicates << ["TITLE", current_title, title_index[current_title], current_entry]
        else
          title_index[current_title] = current_entry
        end
      end

      if current_doi
        if doi_index.key?(current_doi)
          duplicates << ["DOI", current_doi, doi_index[current_doi], current_entry]
        else
          doi_index[current_doi] = current_entry
        end
      end
    end

    current_entry = line.strip
    current_title = nil
    current_doi = nil
  end

  if line =~ /^\s*title\s*=\s*[{"](.+?)[}"],?\s*$/i
    current_title = normalize_title($1)
  end

  if line =~ /^\s*doi\s*=\s*[{"](.+?)[}"],?\s*$/i
    current_doi = $1.strip.downcase
  end
end

unless current_entry.nil?
  if current_title
    if title_index.key?(current_title)
      duplicates << ["TITLE", current_title, title_index[current_title], current_entry]
    else
      title_index[current_title] = current_entry
    end
  end
  if current_doi
    if doi_index.key?(current_doi)
      duplicates << ["DOI", current_doi, doi_index[current_doi], current_entry]
    else
      doi_index[current_doi] = current_entry
    end
  end
end

# Scrive risultati
File.open("duplicates.txt", "w") do |f|
  if duplicates.empty?
    f.puts "No duplicates found."
  else
    duplicates.each do |type, key, first, dup|
      f.puts "DUPLICATE (#{type}): #{key}"
      f.puts "  Original: #{first}"
      f.puts "  Duplicate: #{dup}"
      f.puts
    end
  end
end

puts "Analysis complete. See 'duplicates.txt' for results."
