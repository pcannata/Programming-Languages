package com.example.lambda;

/**
 * @author MikeW
 */
public class RunnableTest {
  public static void main(String[] args) {
    
    System.out.println("=== RunnableTest ===");
    
    // Anonymous Runnable
    Runnable r1 = new Runnable(){
      @Override
      public void run(){
        try {
          Thread.sleep(5000);                 //1000 milliseconds is one second.
        } catch(InterruptedException ex) {
          Thread.currentThread().interrupt();
        }
        System.out.println("Hello world one!");
      }
    };
    
    // Lambda Runnable
    Runnable r2 = () -> {
        try {
            Thread.sleep(1000);                 //1000 milliseconds is one second.
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        ;
        System.out.println("Hello world two!");
    };
    
    // Run em!
    new Thread(r1).start();
    new Thread(r2).start();
    
  }
}
