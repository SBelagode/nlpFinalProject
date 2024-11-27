import pandas as pd


#the language tags we are using are: bg ms ne jv mt ug bo si

# Bulgarian, Indonesian, Nepali, Javanese,  Maltese, Uyghur, Tibetan, Sinhala Respectively. 

# for the specific language, replace the tag before "..."/validation , "..."/train, and "..."/test with the correct language tag


splitsBG = {'validation': 'bg/validation-00000-of-00001.parquet', 'test': 'bg/test-00000-of-00001.parquet', 'train': 'bg/train-00000-of-00001.parquet'}
dfTrainBG = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsBG["train"])
dfValBG = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsBG["validation"])
dfTestBG = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsBG["test"])

print(dfValBG.head())
print(dfValBG.iloc[0,0])

print("Shape of Validation data frame for BG:",dfValBG.shape)


splitsMS= {'validation': 'ms/validation-00000-of-00001.parquet', 'test': 'ms/test-00000-of-00001.parquet', 'train': 'ms/train-00000-of-00001.parquet'}
dfTrainMS = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsMS["train"])
dfValMS = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsMS["validation"])
dfTestMS = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsMS["test"])

splitsNE = {'validation': 'ne/validation-00000-of-00001.parquet', 'test': 'ne/test-00000-of-00001.parquet', 'train': 'ne/train-00000-of-00001.parquet'}
dfTrainNE = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsNE["train"])
dfValNE = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsNE["validation"])
dfTestNE = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsNE["test"])

splitsJV = {'validation': 'jv/validation-00000-of-00001.parquet', 'test': 'jv/test-00000-of-00001.parquet', 'train': 'jv/train-00000-of-00001.parquet'}
dfTrainJV = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsJV["train"])
dfValJV = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsJV["validation"])
dfTestJV = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsJV["test"])

splitsMT = {'validation': 'mt/validation-00000-of-00001.parquet', 'test': 'mt/test-00000-of-00001.parquet', 'train': 'mt/train-00000-of-00001.parquet'}
dfTrainMT = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsMT["train"])
dfValMT = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsMT["validation"])
dfTestMT = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsMT["test"])

splitsUG= {'validation': 'ug/validation-00000-of-00001.parquet', 'test': 'ug/test-00000-of-00001.parquet', 'train': 'ug/train-00000-of-00001.parquet'}
dfTrainUG= pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsUG["train"])
dfValUG= pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsUG["validation"])
dfTestUG = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsUG["test"])

splitsBO = {'validation': 'bo/validation-00000-of-00001.parquet', 'test': 'bo/test-00000-of-00001.parquet', 'train': 'bo/train-00000-of-00001.parquet'}
dfTrainBO = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsBO["train"])
dfValBO = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsBO["validation"])
dfTestBO = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsBO["test"])

splitsSI = {'validation': 'si/validation-00000-of-00001.parquet', 'test': 'si/test-00000-of-00001.parquet', 'train': 'si/train-00000-of-00001.parquet'}
dfTrainSI = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsSI["train"])
dfValSI = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsSI["validation"])
dfTestSI = pd.read_parquet("hf://datasets/unimelb-nlp/wikiann/" + splitsSI["test"])