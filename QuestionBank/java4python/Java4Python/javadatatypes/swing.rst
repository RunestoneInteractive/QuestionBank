.. activecode:: swing
    :author: bmiller
    :difficulty: 3.0
    :basecourse: java4python
    :chapter: Java4Python
    :subchapter: javadatatypes
    :topics: Java4Python/javadatatypes
    :from_source: T
    :language: java
    :sourcefile: TempConvGUI.java

    import javax.swing.*;

    public class TempConvGUI {

        public static void main(String[] args) {
            String fahrString;
            Double fahr, cel;

            fahrString = JOptionPane.showInputDialog("Enter the temperature in F");
            fahr = new Double(fahrString);
            cel = (fahr - 32) * 5.0/9.0;

            JOptionPane.showMessageDialog(null,"The temperature in C is, " + cel);
        }

    }