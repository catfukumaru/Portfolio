import javax.swing.*; // used to make the ui

// makes the window
public class App {
    public static void main(String[] args) throws Exception {
        
        int boardWidth = 360;
        int boardHeight = 640; // the unit is pixels

        JFrame frame = new JFrame("Flappy Bird"); // the window
        
        frame.setSize(boardWidth, boardHeight); // set the size of the window, which mactches the size of the background image
        frame.setLocationRelativeTo(null); // put is at the centre of my scrren
        frame.setResizable(false); // the size of the window cannot be changed by the user
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // the program ends when it is closed

        // add the game to the window
        FlappyBird flappyBird = new FlappyBird();
        frame.add(flappyBird);
        frame.pack(); /// the windows is automatically sized to fit the game
        // Why do you need to use .pack if the window/fram size is equal to the jpanel being added to the?
            // you need to use  .pack() on a window (like a JFrame), it makes the window automatically adjust its size to fit everything inside it correctly, including things like borders and the title bar i.e in this caseif it wasnt there then with size of the window would include the title bar but the size of the jpanel would not. If you set the window size yourself to match just the JPanel, it might not fit right—parts could be cut off, or there might be extra space.
            //Think of .pack() as the method that says: “Make the window just the right size for everything inside, so nothing is missing and it looks good.”
        flappyBird.requestFocus(); // hen an element receives focus, it becomes the recipient of keyboard input or other user interactions.
        frame.setVisible(true); // this always goes at the end. it can be seen
    }
}
