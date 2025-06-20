from google import genai

def get_descricao(modelo,cor):
    prompt = ''' Me mostre uma descrição para venda um sapato do modelo{} na cor {} em apenas 270 caracteres. Fale coisas boas, material,qualidade, bonitas '''
    
    prompt = prompt.format(modelo,cor)
    client = genai.Client(api_key="AIzaSyAzbv2n6uDGK7QVPXK2VIfEE9kX_Xjx7O8")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents= prompt,
    )
    return response.text