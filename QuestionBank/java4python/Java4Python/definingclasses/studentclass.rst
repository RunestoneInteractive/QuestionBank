.. activecode:: studentclass
    :author: bmiller
    :difficulty: 3.0
    :basecourse: java4python
    :chapter: Java4Python
    :subchapter: definingclasses
    :topics: Java4Python/definingclasses
    :from_source: T
    :language: java
    :sourcefile: Student.java

    public class Student {
            public static Integer numStudents = 0;

            private int id;
            private String name;

            public Student(Integer id, String name) {
            this.id = id;
            this.name = name;

            numStudents = numStudents + 1;
            }

            public static void main(String[] args) {
            for(Integer i = 0; i < 10; i++) {
                Student s = new Student(i,"Student"+i.toString());
            }
            System.out.println("The number of students: "+Student.numStudents.toString());
            }
        }