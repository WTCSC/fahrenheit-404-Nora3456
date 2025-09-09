print(f"Welcome to Temperature Converter!")

farenheit_celsius = input("If you are converting Celsius to Farenheit, type 'Farenheit'. If you are converting Farenheit to Celsius, type 'Celsius':")
print(f"*Make sure to type exactly what you'd like to convert, using the same word that's inside the quotations.*") 

if (farenheit_celsius == 'Celsius'):
        Farenheit = int(input("What Farenheit temperature would you like to convert to Celsius?:")) 
        number_c = (Farenheit - 32) * 0.5555
        print(f"{Farenheit}°F converted to Celsius is: {number_c}°C")
        
        
if (farenheit_celsius == 'Farenheit'):
        Celsius = int(input("What Celsius temperature would you like to convert to Farenheit?:") )
        number_C = (Celsius * 1.8) + 32
        print(f"{Celsius}°C converted to Farenheit is:  ")
  
    
        

    

