call cd /d "D:\fb5swans\java\src"
call javac -d D:\fb5swans\test .\javaFB\com\google\flatbuffers\BinaryBuilder.java 
call cd /d "D:\fb5swans\test" 
call java javaFB.com.google.flatbuffers.BinaryBuilder
pause