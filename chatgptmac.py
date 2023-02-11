import openai
import sys
apikey = 'APIKEY'

class Color:
    BOLD = '\033[1m'
    END = '\033[0m'

def intro():
    print(Color.BOLD + '''(ノಠ益ಠ)ノ彡''' + Color.END)

class AI:

    def __init__(self):
        intro()

    def performTask(self, *args):
        # Create prompt string from arguments
        args = ' '.join(sys.argv[1:])
        if len(args) == 0:
            print("Empty prompt")
            return
        # Print prompt string
        print(Color.BOLD + 'Prompt: ' + Color.END + args)
        # print()
        # Authenticate with OpenAI API key
        openai.api_key = apikey
        # Compile request
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=args,
            temperature=0.6,
            max_tokens=4000,
        )
        # Print response
        print(Color.BOLD + 'Response:' + Color.END)
        data = response['choices']
        for key in data:
            print(key['text'])
        print()

myAI = AI()
myAI.performTask()
