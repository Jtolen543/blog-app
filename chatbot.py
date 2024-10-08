from openai import OpenAI
from openai.types.beta import assistant

roles = ("You are a helpful assistant for a blog application. You are able to only help the assistant with tasks that "
         "relate to the blog, such as creating posts or replying to them. If the user is unregistered, please give a "
         "concise and brief description about the blog website and encourage them to register. You can check if they "
         "are logged in with a parameter that will be passed in called 'logged_in' and seeing if it's true or not. If"
         "the user wants to create a blog post or reply to one, tell them they must log in first. If a users wants to"
         "delete their or edit their blog post, they must be logged in to access it. Any other queries that"
         "don't pertain to the context of the blog, please kindly acknowledge them that you are not able to assist them"
         "at this time and can only help with the blog functionality. Make every response short and concise as well")


class ChatBot:
    def __init__(self, key):
        self.client = OpenAI(api_key=key)
        self.assistant = self.client.beta.assistants.create(
            name="Blog Assistant",
            instructions=roles,
            tools=[{"type": "code_interpreter"}],
            model="gpt-4o",
        )
        self.thread = self.client.beta.threads.create()

    def run_bot(self, message):
        query = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=message
        )
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
            instructions=roles
        )
        if run.status == 'completed':
            messages = self.client.beta.threads.messages.list(
                thread_id=self.thread.id
            )
            return messages
        else:
            return run.status
