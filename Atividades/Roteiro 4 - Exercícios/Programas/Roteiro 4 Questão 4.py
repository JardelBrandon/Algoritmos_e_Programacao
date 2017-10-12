#4. Crie um aplicativo de conversão entre as temperaturas Celsius, Farenheit e
#Kelvin. Primeiro o usuário deve escolher se vai entrar com a temperatura em
#Célsius, Farenheit ou Kelvin, em seguida, o usuário deve escolher para qual
#temperatura será feita a conversão. Em seguida, o usuário deve fornecer o
#valor de temperatura a ser convertido.


temperatura = input ("""Digite a letra inicial da temperatura que deseja converter
Considere :
C para (Celcius), F para (Farenheit) e K para (Kelvin) :""")


conversão = input ("""Digite a letra inicial da temperatura para qual deseja realizar a conversão
Considere :
C para (Celcius), F para (Farenheit) e K para (Kelvin) :""")

valor = float (input ("Digite o valor da temperatuta a ser convertido :"))

# Condições :
# Celsius para Celsius
# Celsius para Kelvin
# Celsius para Fahrenheit

# Kelvin para Kelvin
# Kelvin para Fahrenheit
# Kelvin para Celsius

# Fahrenheit para Fahrenheit
# Fahrenheit para Kelvin
# Fahrenheit para Celsius

#Fórmulas das conversões de temperaturas:

#Conversão de	    #para	            #Fórmula
#Grau Celsius       Grau Celsius        ºC = ºC
#Grau Celsius	    kelvin	             K = °C + 273,15
#Grau Celsius	    Grau Fahrenheit	    °F = °C × 1,8 + 32

#Kelvin             Kelvin               K = K
#Kelvin             Grau Fahrenheit     ºF = 1,8 x (K - 273) + 32.
#Kelvin	            Grau Celsius	    °C = K − 273,15

#Grau Fahrenheit	Grau Fahrenheit	    ºF = ºF
#Grau Fahrenheit    Kelvin               K = (y °F + 459,67) x 5/9
#Grau Fahrenheit    Celsius             °C = (°F − 32) / 1,8





if temperatura == "C" and conversão == "C" :
    print ("O valor da temperatura foi de : ", valor,"ºC - Celsius \nConvertido para :", valor,"ºC - Celsius")

elif temperatura == "C" and conversão == "K" :
    convertido = valor + 273.15
    print ("O valor da temperatura foi de : ", valor,"ºC - Celsius \nConvertido para :", convertido,"K - Kelvin")

elif temperatura == "C" and conversão == "F" :
    convertido = valor * 1.8 + 32
    print ("O valor da temperatura foi de: ", valor,"ºC - Celsius \nConvertido para :", convertido,"ºF - Fahrenheit")

elif temperatura == "K" and conversão == "K" :
    print ("O valor da temperatura foi de : ", valor,"K - Kelvin \nConvertido para :", valor,"K - Kelvin")

elif temperatura == "K" and conversão == "F" :
    convertido = 1.8 * (valor - 273.15) + 32
    print ("O valor da temperatura foi de : ", valor,"K - Kelvin \nConvertido para :", convertido,"ºF - Fahrenheit")

elif temperatura == "K" and conversão == "C" :
    convertido = valor - 273.15
    print ("O valor da temperatura foi de : ", valor,"K - Kelvin \nConvertido para :", convertido,"ºC - Celsius")

elif temperatura == "F" and conversão == "F" :
    print ("O valor da temperatura foi de : ", valor,"ºF - Fahrenheit \nConvertido para :", valor,"ºF - Fahrenheit")

elif temperatura == "F" and conversão == "K" :
    convertido = (valor + 459.67) * 5 / 9
    print ("O valor da temperatura foi de : ", valor,"ºF - Fahrenheit \nConvertido para :", convertido,"K - Kelvin")

elif temperatura == "F" and conversão == "C":
    convertido = (valor - 32) / 1.8
    print ("O valor da temperatura foi de : ", valor, "ºF - Fahrenheit \nConvertido para :", convertido,"ºC - Celsius")

else :
    print ("Inválido !")


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada da Inicias das temperaturas a serem convertidas e o valor para a conversão
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as conversões pedidas na questão, realizando-as com suas respectivas fórmulas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas


