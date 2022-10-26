/*
This is a simple 21 game base on Resident Evil 7 21 DLC
Play against computer that makes own decisions
*/

import java.util.*;

public class SimpleGame
{
    int player = 0;
    int computer = 0;
    List<String> p = new ArrayList();
    List<String> c = new ArrayList();
    String decision_player = "";
    String decision_computer = "";
    List<Integer> numbers = new ArrayList(); // Decks of playing cards to be drawn
    boolean current = true;
    boolean decision = false; // If both chose N then close game
    Scanner sc = new Scanner(System.in);
    
    // Main game function
    public static void main(String[] args){
        SimpleGame self = new SimpleGame();
        
        self.initialise();
        System.out.println("Start of the game...");
        
        while(self.player < 22 && self.computer < 22 && self.decision == false){
            System.out.println("................................");
            System.out.println("This are the current decks...");
            System.out.println(self.numbers);
            System.out.println(self.c);
            System.out.println(self.p);
            
            if(self.current == true)
            {
                System.out.println("Computer thinks...");
                float above = 0f;
                float below = 0f;
                
                for (int i = 0; i < self.numbers.size(); i++){           
                    if ((self.numbers.get(i) + self.computer) > 22){
                        above++;
                    } else if ((self.numbers.get(i) + self.computer) < 22){
                        below++;
                    } else {
                        continue;
                    }   
                }
                System.out.println(above + "  " + below);
                
                if ((above - 1) > below && self.computer < self.player){
                    self.decision_computer = "N" ;
                    System.out.println("Computer passes");
                    self.current = false;
                } else if ((above + 2) <= below && self.computer > self.player){
                    int computer_draw = self.generate(self.numbers);
                    self.computer = self.computer + computer_draw;
                    self.c.add(String.valueOf(computer_draw));
                    System.out.println("Computer draws - "+computer_draw);
                    self.current = false;
                } else if (self.computer > self.player){
                    self.decision_computer = "N" ;
                    System.out.println("Computer passes");
                    self.current = false;
                } else if (self.computer == self.player && above < below){
                    int computer_draw = self.generate(self.numbers);
                    self.computer = self.computer + computer_draw;
                    self.c.add(String.valueOf(computer_draw));
                    System.out.println("Computer draws - "+computer_draw);
                    self.current = false;
                } else {
                    self.decision_computer = "N" ;
                    System.out.println("Computer passes");
                    self.current = false;
                }
     
            } else {
                System.out.println("Player turn do you want to draw card: ");
                self.decision_player = self.sc.nextLine();
                
                if(self.decision_player.equals("Y"))
                {
                    int player_draw = self.generate(self.numbers);
                    self.player = self.player + player_draw;
                    self.p.add(String.valueOf(player_draw));
                    System.out.println("Player draws - " + player_draw);
                    self.current = true;
                    
                } else {
                    self.decision_player = "N";
                    self.current = true;
                }
            }

            if (self.decision_player.equals("N") && self.decision_computer.equals("N"))
            {
                self.decision = true;
            } 
        } 
      
        self.finalise();
        System.out.println(self.c);
        System.out.println(self.p);
        if (self.computer < self.player && self.player < 22){
            System.out.println("Player Wins");
        } else if (self.computer < self.player && self.player > 21){
            System.out.println("Computer Wins");
        } else if (self.computer > self.player && self.computer < 22){
            System.out.println("Computer Wins");
        } else {
            System.out.println("Player Wins");
        }
        System.out.println("Game Over");
    }
    
    // Generates the drawing deck
    public void initialise(){     
        for(int i = 1; i <=11; i++){
            numbers.add(i);
        }
        
        for(int i = 0; i < 2; i++){
            //Generates initial list for player
            int generated_player = generate(numbers);
            player = player + generated_player;
            p.add(String.valueOf(generated_player));
            
            //Generates initial list for computer
            if(i == 1)
            {
                int generated_computer = generate(numbers);
                computer = computer + generated_computer;
                c.add(String.valueOf(generated_computer));
            } else {
                c.add("*");
                int genenerated_computer2 = generate(numbers);
                computer = computer + genenerated_computer2;
            }
        }    
    }
    
    // Used to remove the * from the computer List
    public void finalise(){
        int temp = computer;
        
        for (int i = 1; i < c.size(); i++) {
            temp = temp - Integer.valueOf(c.get(i));
        }
        c.set(0, String.valueOf(temp));
        
    }
    
    // Draws a random number from the playing deck and removes it
    public int generate(List possible){
        Random rand = new Random();
        int generated = (int) possible.get(rand.nextInt(possible.size()));
        possible.remove(Integer.valueOf(generated));
        return generated; 
    }
}
