#!/usr/bin/env ruby
# Script per trovare entry duplicate in un file .bib usando il campo title come chiave
# Uso: ruby find_bib_duplicates.rb biblio.bib

require 'set'

if ARGV.empty?
  puts "Uso: ruby #{__FILE__} file.bib"
  exit 1
end

bibfile = ARGV[0]
unless File.exist?(bibfile)
  puts "File #{bibfile} non trovato!"
  exit 1
end

entries = {}
duplicates = {}

current_entry = nil
current_title = nil

File.foreach(bibfile) do |line|
  if line.strip.start_with?('@')
    current_entry = line.strip
    current_title = nil
  end

  if line =~ /^\s*title\s*=\s*[{"](.+?)[}"],?\s*$/i
    title = $1.strip.downcase
    if entries.key?(title)
      duplicates[title] ||= []
      duplicates[title] << current_entry
    else
      entries[title] = current_entry
    end
    current_title = title
  end
end

File.open("duplicates.txt", "w") do |f|
  if duplicates.empty?
    f.puts "No duplicates found"
  else
    duplicates.each do |title, entries_list|
      f.puts "TITLE: #{title}"
      f.puts "  Entry original: #{entries[title]}"
      entries_list.each { |entry| f.puts "  Duplicate: #{entry}" }
      f.puts
    end
  end
end

puts "Analysis complete. Check 'duplicates.txt' for results."
