import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class AdventPart1 {
    
    public static void main(String[] args) {

        int leftSide [];
        int rightSide [];


        try {
            String content = Files.readString(Path.of("1-advent.txt"));
            
            String input [] = content.split(content);

            System.out.println(input);

            

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    
}
