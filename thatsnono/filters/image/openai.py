import base64
import requests
import val

def captionize_img(base64_image: str):
    """
    base64 encoding 헤드포함해서 넘겨야 함
    """
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {val.OPENAI_API_KEY}"
    }

    payload = {
      "model": "gpt-4-vision-preview",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "이 이미지에 대해서 설명해줘"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    caption = response.json()['choices'][0]['message']['content']
    return caption

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# main
if __name__ == "__main__":
    pass
