# Bot para Pechincha do AliExpress
Esse bot serve para se "auto-ajudar" no evento Pechincha do AliExpress. **Isso é contra os termos de uso, não me responsabilizo caso sua conta seja suspensa, use por conta e risco//em contas alternativas!**  
*Pechinchas de nível "fácil" você consegue sem usar proxy/rotacionar dispositivo desde que não esteja atrás de um cgnat, Pechinchas de nível médio é necessário rotacionar por proxies e dispositivos*  
### Como usar:  
1. Instale o [Python](https://www.python.org/downloads/)  
  -**MARQUE A CAIXINHA PARA ADICIONAR O PYTHON AO PATH!**  
2. Instale o Selenium, para isso abra um CMD **novo** e digite o comando: ```pip install selenium```  
3. Se já não tiver no sistema, instale o [Google Chrome](https://www.google.com/chrome/)  
4. Abra o Chrome e vá para: [chrome://version](chrome://version)  
5. Oberse o primeiro par de números na primeira linha (11.05.2020, provavelmente é 90), vá para o [site de download do chromedriver](https://chromedriver.chromium.org/downloads) e baixe a versão correspondente ao seu sistema, extraia o executável para a mesma pasta onde o arquivo **bot.py** disponível aqui se encontra no seu computador.  
6. Edite o arquivo **bot.py** com o bloco de notas e substitua o link na primeira linha. **MANTENHA AS ASPAS!**  
7. No CMD, use o comando ```cd Caminho/Para/A/Pasta``` para navegar até a pasta que tem o bot e o chromedriver, uma vez dentro dela, use o comando ```python3 bot.py``` para rodar.  
#### Sobre Proxies e Dispositivos...
* Para a maior segurança possível que seus pedidos não sejam bloqueados, faça o uso de proxies no programa. Para isso, é necessário criar um arquivo chamado ```proxylist.txt``` na mesma pasta onde o bot está, adicione os proxies no arquivo linha por linha no formato ```IP:PORTA``` que é a síntaxe HTTP, por exemplo: ```127.0.0.1:80```, onde *127.0.0.1* é o IP e *80* é a porta, repare os **:**. Importante ressaltar que o Pechincha é bloqueado em alguns países, se usar proxy desses países você terá erro naquela tentativa!  
* Para dispositivos, isso varia de acordo com a versão que está usando, crie um arquivo chamado ```devicelist.txt``` na mesma pasta onde o bot está e adicione o nome de um dispositivo **mobile** em cada linha, o arquivo **opt_devicelist.txt** tem uma lista dos que funcionam para a minha versão, use-a como base e o mais importante: *pesquise sobre a sua versão do Chrome!*  [Este link possui uma listinha com alguns que você pode tentar.](https://www.browserstack.com/list-of-browsers-and-platforms/automate)
