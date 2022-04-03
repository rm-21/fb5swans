# fb5swans

The library aims to use java and Python alongside the FlatBuffers (FB) Serialiszation Library by Google.

The data is encoded by Java and decoded by Python. This was a design decision since FB currently doesn't support mutating FlatBuffers for Python. Therefore, encoding is mutable, however, decoding would require API regeneration each time a `schema` is updated.

# Steps to Use It
1. Clone the Repository on your local system.
2. Navigate to `fb5swans/app/fb_encoder.bat`:
    * In line 1, modify the path to the java src folder as per your local system.
    * In line 2, add your desired test path followed by `-d` toggle.
    * In line 2, the second path is the raw `BinaryBuilder.java` file that will produce the encoded `.bin` file as per the schema. The output will be in the path as per the desired test path above.
    * In line 3, update the path after `/d` toggle to the test path in line 2.
    * Do not edit line 4.
    * Close the file and run.
3. Navigate to `fb5swans/app/fb_decoder.bat`:
    * Open a terminal in `fb5swans/app`.
    * Run the command `fb_decoder.bat %1 %2`
    * `%1` - location of python folder of fb5swans || `%2` - location of the folder containing the `.bin` files.

# Expected Output
```python
(['FightClub', 24.5, 107.0, ['Ram', 'Shayam', 'Raghuveer']], [['Ram', 24.0, 100.0, 'Male'], ['Shayam', 24.5, 110.0, 'Female'], ['Raghuveer', 25.0, 111.0, 'Male'])
['Ram', 21.0, 76.5, 'Male']
['Shayam', 24.5, 110.0, 'Female']
```

* `line[0][0]` contains the details of the `Client`, `Group` - `FightClub`. `line[0][1]` contains the details of each individual member.
* `line[2]` and `line[2]` contains the details of the `Client`, `Individual`.

# Modifications
1. Navigate to the `fb5swans/java/src/javaFB/com/google/flatbuffers/BinaryBuilder.java` on your local system. This file contains the code to build the `.bin` files.
2. In the `main` method, you will see multiple `byte[] <arrName>`. The `buildIndividual` function builds a single Client. The `buildGroup` function takes a creates a vector of multiple individuals. The attributes, namely, `names`, `age`, `weight`, `g <gender>`, need to passed as arrays with appropriate types as indicated in the example.

# Brief Explanation
1. When you run the `fb_encoder.bat` file, it compiles this `.java` file. Then it creates a `.class` file of the same name. When you run the `.class` file, you will get the appropriate `.bin` files.
2. The `.bin` files can be decoded and read into Python using the `fb_decoder.bat` file. This executes a simple Python files, that reads the `.bin` file as per the generated schema. The schema is stored in `schema` folder as `.fbs` files.
3. The Python file, requires API files generated from the schema, to be able to read the `.bin` buffer with direct access to attribues.