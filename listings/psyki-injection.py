import pandas as pd
from tensorflow.keras.models import Model
from psyki.logic import Theory
from psyki.ski import Injector


def create_uneducated_predictor() -> Model:
...

dataset = pd.read_csv("path_to_dataset.csv")  # load dataset
knowledge_file = "path_to_knowledge_file.pl"  # load knowledge
theory = Theory(knowledge_file, dataset)      # create a theory
uneducated = create_uneducated_predictor()    # create a NN
injector = Injector.kins(uneducated)          # create an injector
educated = injector.inject(theory)            # inject knowledge into the NN

# From now on you can use the educated predictor
# as you would use the uneducated one