from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI

def main():
    try:
        
        # connect to the project
        project_endpoint = "https://sneyd-mijfcka6-swedencentral.cognitiveservices.azure.com/"
        project_client = AIProjectClient(            
                credential=DefaultAzureCredential(
                    exclude_environment_credential=True,
                    exclude_managed_identity_credential=True,),
                endpoint=project_endpoint,
            )
        
        # Get a chat client
        chat_client = project_client.get_openai_client(api_version="2024-12-01-preview")

        prompt = [
                {"role": "system", "content": "You are a helpful AI assistant that answers questions."}            
            ]
        
        # Get a chat completion based on a user-provided prompt
        user_prompt = input("Enter a question:")

        prompt.append({"role": "user", "content": user_prompt})
        
        response = chat_client.chat.completions.create(
            model="gpt-4o",
            messages = prompt
        )

        completion = response.choices[0].message.content

        print(completion)
        prompt.append({"role": "assistant", "content": completion})

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()