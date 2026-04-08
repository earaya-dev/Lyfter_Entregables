1\. Inicio

2\. Defina **precio de producto**

3\. Defina **porcentaje1**

4\. Defina **porcentaje2**

5\. Defina **precio final**

6\. Mostrar "Ingrese el precio de producto"

7\. Pedir **precio de producto**

8\. porcentaje1 = 0.02

9\. porcentaje2 = 0.10

10\. precio final = 0



11\. Si (**precio de producto** < 100) entonces

&nbsp;    **descuento = precio de producto * porcentaje1**
&nbsp;	 **precio final = precio de producto - descuento**



&nbsp;  Sino Si (**precio de producto** >= 100) entonces

&nbsp;    **descuento = precio de producto * porcentaje2**
&nbsp;	 **precio final = precio de producto - descuento**



   Sino

&nbsp;	 Mostrar "Para calcular el precio final, el precio de producto no puede ser negativo"

   Fin Si



12\. Mostrar "El precio final es de: + **precio final**"



13.Fin















1. Inicio
2. Defina **tiempo en segundos**
3. Defina **tiempo estático en segundos**
4. Defina **tiempo residuo**
5. Mostrar "Ingrese el tiempo en segundos"
6. Pedir t**iempo en segundos**
7. **tiempo estático en segundos = 10 \* 60**
8. **tiempo residuo = 0**
   
9. Si (**tiempo en segundos** < **tiempo estático en segundos**) entonces

       **tiempo residuo = tiempo estático en segundos - tiempo en segundos**		

&nbsp;      Mostrar "Los segundos que faltarían para llegar a 10 minutos es:", **tiempo residuo**



   Sino Si (**tiempo en segundos > tiempo estático en segundos)** entonces

&nbsp;      Mostrar "Mayor"



&nbsp;  Sino 

&nbsp;      Mostrar "Igual"

&nbsp;  

&nbsp;  Fin Si



10\. Fin











1. Inicio
2. Defina **Numero de Usuario**
3. Defina **contador**
4. Defina **acumulación**
5. Mostrar "Ingrese el numero deseado"
6. Pedir **Numero de Usuario**
7. **Contador = 1**
8. **acumulación = 0**



7\. Mientras que (**contador <= Numero de Usuario)**

     **acumulación = acumulación + contador**

     **contador = contador + 1**



   Fin Mientras



8\. Mostrar acumulación



9\. Fin

&nbsp;	

