import streamlit.components.v1 as components

def load_botpress_chatbot():
    botpress_html = """
    <script src="https://cdn.botpress.cloud/webchat/v3.1/inject.js"></script>
    <div id="webchat" style="width: 100%; height: 500px;"></div>
    <script>
        window.botpress.init({
            "botId": "4c16e82b-cf37-4278-a18a-4d46230cba9b",
            "clientId": "979abd7d-57cc-4aed-932e-a0c45463d640",
            "selector": "#webchat",
            "configuration": {
                "version": "v1",
                "botName": "EduBridgeAI",
                "botAvatar": "https://files.bpcontent.cloud/2025/07/10/10/20250710100553-FGW84Q6W.jpeg",
                "botDescription": "This Bot is just used for feedback purposes.....",
                "fabImage": "https://files.bpcontent.cloud/2025/07/09/16/20250709165939-A0Q3O1OH.png",
                "color": "#1e5bc4",
                "variant": "solid",
                "headerVariant": "glass",
                "themeMode": "light",
                "fontFamily": "inter",
                "radius": 4,
                "feedbackEnabled": true,
                "footer": "[⚡ by Botpress](https://botpress.com/?from=webchat)",
                "allowFileUpload": true,
                "storageLocation": "localStorage"
            }
        });
    </script>
    """
    components.html(botpress_html, height=500)
