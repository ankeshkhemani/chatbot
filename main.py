import json

class Stage():

    def __init__(self,conversationContext,stageDict):
        self.stageDict = stageDict
        # Fetch the parent object of the Conversation Class for context
        self.conversationContext = conversationContext

    def executeStage(self):
        # Replace this code with actual logic
        print (self.stageDict)


class Conversation():

    def __init__(self,stageList):
        self.stages = []

        # create a list of Stage objects corresponding to each stage in input json
        for serialNo in range(len(stageList)):
            self.stages.append(Stage(self,stageList[serialNo]))

    def start(self):

        # execute each stage from the stages list
        for stage in self.stages:
            stepDone = False

            # While loop ensures a stage is re-run if there is any error during stage.
            while (stepDone!=True):
                try:
                    # execute the stage
                    stage.executeStage()
                    stepDone = True
                except:
                    stepDone = False


def startConversation(jsonFilePath):

    # Open Json
    with open(jsonFilePath) as json_data:
        inputJson = json.load(json_data)

    # If function attribute matches then create a Conversation object and start conversation
    if (inputJson['function']== "sample-text-function"):
        conversation = Conversation(inputJson['questions'])
        conversation.start()


if __name__ == '__main__':
    # Starts a conversation based on assignment_1_input_1.json
    startConversation("test_input_json/assignment_1_input_1.json")