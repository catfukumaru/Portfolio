import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;
import javax.swing.*;

// when drawing itstarts from the top left corner 
//------------------------------------
// simbol name_game
//------------------------------------
//*(here at 0,0)                      |
//                                    |

public class FlappyBird extends JPanel implements ActionListener, KeyListener{
    // i am making what goes into the window
    // it keeps the jpanel features while being able to add features to it

    int boardWidth = 360;
    int boardHeight = 640;

    // Image variables
    Image backgroundImage;
    Image birdImage;
    Image topPipeImage;
    Image bottomPipeImage;
    

    // bird variables
    int birdX = boardWidth/8; // x coor
    int birdY = boardHeight/2;  // y coor
    int birdWidth = 34;
    int birdHeight = 24;

    class Bird{
        int x = birdX;
        int y = birdY;
        int width = birdWidth;
        int height = birdHeight;

        Image img;

        Bird(Image img) {
            this.img = img;
        }
    }


    //Pipes
    int pipeX = boardWidth;
    int pipeY = 0;
    // right top side

    int pipeWidth = 64;//scaled 1/6
    int pipeHeight = 512;

    class Pipe{
        int x = pipeX;
        int y = pipeY;
        int width = pipeWidth;
        int height = pipeHeight;
        Image img;
        boolean passed = false; // see if the bird passed the pipe


        Pipe(Image img){
            this.img = img;
        }
    }









    // game logic

    Bird bird;
    int velocityY = -6; // number of pixels the image goes up in each frame
    int gravity = 1;

    Timer gameLoop;
    Timer placePipesTimer;

    int velocityX = -4;// for the pipes
    ArrayList<Pipe> pipes;
    // chnage the position of each pipe
    Random random = new Random();

    boolean gameOver = false; // if false you can still play
    double score = 0;












    FlappyBird(){
        setPreferredSize(new Dimension(boardWidth, boardHeight));
        setBackground(Color.blue);
        setFocusable(true); // makes sure the main japnel takes the key events
        addKeyListener(this); // cheks the key pressed, typed and released

        // The code locates the image file relative to the class, loads it as an ImageIcon, then pulls out the underlying Image and puts it into the variable backgroundImage for use in your program.
        backgroundImage = new ImageIcon(getClass().getResource("./flappybirdbg.png")).getImage();
        birdImage = new ImageIcon(getClass().getResource("./flappybird.png")).getImage();
        topPipeImage = new ImageIcon(getClass().getResource("./toppipe.png")).getImage();
        bottomPipeImage = new ImageIcon(getClass().getResource("./bottompipe.png")).getImage();
        
        
        
        //new ImageIcon(...)
        // This creates a new ImageIcon object. ImageIcon is a Java class from the Swing library that can hold and display images such as PNG, GIF, or JPEG files.

        // getClass().getResource("./flappybird.png")

        // getClass() gets the Class object for the current class (where this code runs).

        // .getResource("./flappybird.png") looks for a file called "flappybird.png" in the same location (folder) as the class file. It returns a URL pointing to the image if it exists.

        // ImageIcon(getClass().getResource("./flappybird.png"))
        // This constructs an ImageIcon using the URL to "flappybird.png." If the image is not found at that location, the returned ImageIcon will be empty (no image will be shown).

        // .getImage()
        // This method extracts the actual Image (a generic image object Java can work with, not just for displaying in Swing) from the ImageIcon.
   

        bird = new Bird(birdImage);
        pipes = new ArrayList<Pipe>();

        placePipesTimer = new Timer(1500, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                placePipes();
            }
        } ); 
        

        placePipesTimer.start();

        // game timer
        gameLoop = new Timer(1000/60, this); // 1000 == 1 second divs 60 cause we want 60 frames per second
        gameLoop.start();
    }


    public void placePipes(){
        int randomPipeY = (int)(pipeY - pipeHeight/4 - Math.random() * (pipeHeight/2));
        // stopped 40:20                 // quater of the pipe height when pipe y is 0
        // or 3/4 of pipe height if pipe y is 1
        //  Math.random(): Returns a random double value between 0.0 (inclusive) and 1.0 (exclusive).
        // pipeY: This is likely the starting vertical position at 0,0
        // pipeHeight/2: Half the pipe’s height.

        //Math.random() * (pipeHeight/2): Generates a random double between 0 and half the pipe’s height.

        //pipeY - pipeHeight/4: Offsets the pipeY starting value by a quarter of the pipe’s height upwards.
        //The expression calculates a random vertical position for a pipe by subtracting a random value (between 0 and half the pipe’s height) and a fixed value (quarter pipeHeight) from pipeY.

        // (int) casts the result to an integer (since coordinates are usually integers).
        
        int openingSpace = boardHeight/4; // space for the bitd to go past 
        
        Pipe topPipe = new Pipe(topPipeImage);
        topPipe.y = randomPipeY;
        Pipe bottomPipe = new Pipe(bottomPipeImage);
        bottomPipe.y = topPipe.y+ pipeHeight + openingSpace;
        //top of the pipe hieght, , bottom of the pipe hieght, the gapt inbetween the pipes

        pipes.add(topPipe);
        pipes.add(bottomPipe);
    }

    // but he images on the background
    public void paintComponent(Graphics g){
    //Graphics class in Java is an abstract class that provides the basic methods and context needed to draw shapes, text, and images on components or images in a graphical user interface

        super.paintComponent(g); // a method in Java Swing that you override to draw or paint anything (like images or shapes) on a component, allowing you to control exactly what appears inside that component whenever it needs to be shown or refreshed
        // inherits the draw function from Jpanel
        draw(g);
    }

    public void draw(Graphics g){
        
        g.drawImage(backgroundImage, 0, 0, boardWidth, boardHeight, null);
        //  "put a picture on the screen" at a certain spot inside your program's window. 
        g.drawImage(bird.img, bird.x, bird.y, bird.width, bird.height, null);
        for (int i = 0; i < pipes.size(); i++){
            Pipe pipe = pipes.get(i);
            g.drawImage(pipe.img, pipe.x, pipe.y, pipe.width, pipe.height, null);
        }


        //score
        g.setColor(Color.WHITE);
        g.setFont(new Font("Arial", Font.PLAIN, 32));
        if (gameOver){
            g.drawString("Game Over: " + String.valueOf((int) score), 10, 35);
        }
        else{
             g.drawString(String.valueOf((int) score), 10, 35);
        }
    }   


    public void move(){
        // bird
        velocityY+=gravity;
        bird.y+= velocityY; // update the speed of the bird
        bird.y = Math.max(bird.y, 0); // stays not go past the top of the backgroud image
    
        //pipes
        for (int i = 0; i < pipes.size(); i++){
            Pipe pipe = pipes.get(i);
            pipe.x+= velocityX;
            
            if (!pipe.passed && bird.x > pipe.x + pipe.width){
                // if the pipe is not passed and the bir'ds passes the right side of the pipe
                pipe.passed = true;
                score +=0.5; // 0.5 for passing 1 pipe
            }

            if (collision(bird, pipe)){
                gameOver = true;
            }
        }

        if (bird.y > boardHeight){
            gameOver = true;
        }
    
    }




    public boolean collision(Bird a, Pipe b){
        // This code checks if two rectangles—representing a Bird (a) and a Pipe (b)—are colliding or overlapping
        return a.x < b.x + b.width && // Checks if the left edge of Bird is to the left of the right edge of Pipe.
        a.x + a.width > b.x && //  Checks if the right edge of Bird is to the right of the left edge of Pipe.
        a.y < b.y + b.height && //Checks if the top edge of Bird is above the bottom edge of Pipe.
        a.y + a.height > b.y; //Checks if the bottom edge of Bird is below the top edge of Pipe.

//         This is a classic axis-aligned bounding box (AABB) collision detection method.

        // It works by making sure there is no gap between any side of the two rectangles: if there’s no gap, then the rectangles are overlapping (colliding).



    }

    //
    //keys
    //

    @Override
    public void actionPerformed(ActionEvent e) {
        // what get done 60 times a second, ie putting things on the screen
        move();
        repaint();
        if (gameOver){ // if the bird falls doown or goes so hight that it is outside the game then game over
            placePipesTimer.stop(); // stop adding pipes
            gameLoop.stop(); // stops updating the frames of the game
        }

    }
        
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_SPACE){
            velocityY = -9;

            if (gameOver){
                // restart the game by resting the game to its default values
                bird.y = birdY;
                velocityY = 0;
                pipes.clear();
                score = 0;
                gameOver= false;
                gameLoop.start();
                placePipesTimer.start();
            }
        }
    }
    @Override
    public void keyTyped(KeyEvent e) {
       
    }
    @Override
    public void keyReleased(KeyEvent e) {
       
    }

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    
     
}


