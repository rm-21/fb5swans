package javaFB.com.google.flatbuffers;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class BinaryBuilder {
    public static void main(String[] args) {
        byte[] person1 = buildIndividual("Ram", 21, 76.5f, Gender.Male);
        writeToBinary(person1, "individual1");

        byte[] person2 = buildIndividual("Shayam", 24.5f, 110.0f, Gender.Male);
        writeToBinary(person1, "individual2");

        CharSequence[] names = {"Ram", "Shayam", "Raghuveer"};
        float[] age = {24.0f, 24.5f, 25.0f};
        float[] weight = {100.0f, 110.0f, 111.0f};
        byte[] g = {Gender.Male, Gender.Female, Gender.Male};
        byte[] group1 = buildGroup("FightClub", names, age, weight, g);
        writeToBinary(group1, "group1");
    }

    private static byte[] buildIndividual(CharSequence s, float age, float weight, byte g) {
        FlatBufferBuilder builder = new FlatBufferBuilder(0);

        // Create Person
        int person = Person.createPerson(builder, false, builder.createString(s), age, weight, g);
        builder.finish(person);

        // Byte-array
        return builder.sizedByteArray();
    }

    private static byte[] buildGroup(CharSequence groupName, CharSequence[] peopleNames,
                                     float[] age, float[] weight, byte[] g) {
        FlatBufferBuilder builder = new FlatBufferBuilder(0);

        // Name
        int name = builder.createString(groupName);

        //Check
        if (age.length != weight.length || age.length != g.length || age.length != peopleNames.length)
            return new byte[]{};

        //Average age
        float avgAge = 0;
        for (float a: age) {
            avgAge += a;
        }
        avgAge /= age.length;

        //Average weight
        float avgWeight = 0;
        for (float w: weight) {
            avgWeight += w;
        }
        avgWeight /= weight.length;

        // People Vector
        int[] peeps = new int[age.length];
        for (int i = 0; i < peeps.length; i++) {
            peeps[i] = Person.createPerson(builder, false, builder.createString(peopleNames[i]), age[i], weight[i], g[i]);
        }
        int people = Group.createPeopleVector(builder, peeps);

        // End Builder
        int groupBuild = Group.createGroup(builder, true, name, avgAge, avgWeight, people);
        builder.finish(groupBuild);

        // Byte-array
        return builder.sizedByteArray();
    }

    private static void writeToBinary(byte[] buffer, String type) {
        {
            Path path = Paths.get(type + "Binary.bin");
            try {
                Files.write(path, buffer);
                System.out.println("Successfully written data to the file " + type + "Binary.bin");
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
