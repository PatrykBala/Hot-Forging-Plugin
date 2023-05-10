# Hot Forging Plugin for Abaqus.
![image](https://user-images.githubusercontent.com/73967948/174500219-1b857f8b-1b53-4c76-b0c3-057e0d2ce33e.png)

## General info
A plug-in for the Simulia Abaqus application that automatically prepares a numerical model of the cylinder. A plug with GUI that prepares and then runs simulation of upsetting a cylinder-shaped sample with dimensions and material properties specified by the user. The plug-in allows you to select the output data to be taken from the mesh nodes (stress, strain, displacement). After the simulation, selected output data is saved to a file or text files. An interface that allows you to enter basic parameters for simulation, such as: part dimensions, boundary conditions, properties and material properties of parts. Option to select the output data to be written to a text file. Validation of the data entered into the model. 

<sub> PL: Wtyczka (ang. plugin) dla aplikacji Simulia Abaqus, która w sposób automatyczny przygotowuje model numeryczny walca.
Wtyczka z GUI przygotowująca, a następnie uruchamiający symulację spęczania próbki w kształcie walca o podanych przez użytkownika wymiarach i własnościach materiałowych. Wtyczka pozwala na wybór danych wyjściowych, które zostaną pobrane z węzłów siatki (naprężenie, odkształcenie, przemieszczenie). Po wykonanej symulacji następuje zapis wybranych danych wyjściowych do pliku lub plików tekstowych.Interfejs umożliwiający wprowadzenie podstawowych parametrów dla symulacji, takich jak: wymiary części, warunki brzegowe, własności i właściwości materiałowe części. Możliwość wyboru danych wyjściowych, które zostaną zapisane do pliku tekstowego. Walidacja wprowadzonych do modelu danych. </sub>

## Technologies
*Abaqus* plug-in created using *Python*.

## Setup
1. **Extract** the archive to the folder with *Abaqus* plugins (*abaqus_plugin*).
2. **Run** the *Abaqus* program.
3. On the toolbar, **expand** the *Plug-in* tab and then **launch** the *Hot Forging* plugin.
4. **Set** the parameters or use default.
5. Start the calculation - **press** *OK* button.
