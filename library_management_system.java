import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;
public class library_management_system {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        library_management_system lib = new library_management_system();
        ArrayList<String> avlblbook = new ArrayList<>(10);
        avlblbook.add("Math");
        avlblbook.add("Geography");
        avlblbook.add("Science");
        avlblbook.add("History");
        avlblbook.add("Biology");
        ArrayList<String> issuedbook = new ArrayList<>();

        System.out.println("1. User");
        System.out.println("2. Customer");

        while (true){
            try {
                int p = input.nextInt();
                if(p == 1){
                    System.out.println("1. Add Book");
                    System.out.println("2. View Available Book");
                    System.out.println("3. Remove Book");
                    int k = input.nextInt();
                    if(k == 1){
                        System.out.println("enter book name ");
                        String bn = input.next();
                        boolean vacancy = false;
                        for(int i = 0; i< 10; i++){
                            if(avlblbook.size() < 10){
                                vacancy = true;
                                break;
                            }
                        }
                        if(vacancy == true && !avlblbook.contains(bn) && !issuedbook.contains(bn)){
                            avlblbook.add(bn);
                            System.out.println("book added");
                        }
                        else{
                            if(vacancy == false){
                                System.out.println("No Vacancy");
                                System.out.println(avlblbook);
                            }
                            else if (avlblbook.contains(bn)) {
                                System.out.println("Book Already There");
                                System.out.println(avlblbook);
                            }
                            else if (issuedbook.contains(bn)) {
                                System.out.println("Book is there...currently issued by some one");
                                System.out.println(issuedbook);
                            }
                        }
                    }
                    else if (k == 2) {
                        System.out.println(avlblbook);
                    }
                    else if (k == 3) {
                        System.out.println("Enter Book Name");
                        String rbn = input.next();
                        if(avlblbook.contains(rbn)){
                            avlblbook.remove(rbn);
                            System.out.println("Book removed");
                            System.out.println(avlblbook);
                        }
                        else{
                            if(issuedbook.contains(rbn)){
                                System.out.println("Book is issued to " + issuedbook.get((issuedbook.indexOf(rbn))+1));
                            }
                            else{
                                System.out.println("book is not available");
                            }
                        }
                    }
                    else {
                        System.out.println("enter valid opt");
                    }

                }
                else if(p == 2){
                    System.out.println("1. Issue book");
                    System.out.println("2. Return book");
                    System.out.println("3. View Available Book");
                    System.out.println("4. View Issued Book");
                    int d = input.nextInt();
                    if(d == 1){
                        System.out.println("Enter book name");
                        String in = input.next();
                        String name;
                        if(avlblbook.contains(in)){
                            System.out.println("enter your name");
                            name = input.next();
                            avlblbook.remove(in);
                            issuedbook.add(in);
                            issuedbook.add(issuedbook.indexOf(in)+1, name);
                            System.out.println("Book is issued to " + name);
                        }
                        else{
                            if(issuedbook.contains(in)){
                                System.out.println("book is already issued to " + issuedbook.get(issuedbook.indexOf(in)+1));
                            }
                            else {
                                System.out.println("Book is not avlbl");
                            }
                        }
                    }
                    else if(d == 2){
                        if(issuedbook.isEmpty()){
                            System.out.println("No book is issued yet");
                        }
                        else{
                            System.out.println("enter book name");
                            String rb = input.next();
                            if(issuedbook.contains(rb)){
                                System.out.println("enter your name");
                                String name = input.next();
                                int x = issuedbook.indexOf(rb);
                                if(issuedbook.get(x+1).equals(name)){
                                    if(avlblbook.size() < 10){
                                        avlblbook.add(rb);
                                        issuedbook.remove(x+1);
                                        issuedbook.remove(rb);
                                        System.out.println("book returned");
                                    }
                                    else {
                                        System.out.println("No space Vacant, Try again Later");
                                    }
                                }
                                else{
                                    System.out.println("Details not matched !!");
                                }
                            }
                            else{
                                System.out.println("book is not issued");
                            }
                        }

                    }
                    else if(d == 3){
                        System.out.println(avlblbook);
                    }
                    else if (d == 4) {
                        System.out.println(issuedbook);

                    } else{
                        System.out.println("please enter a valid option");
                    }
                }
                else{
                    System.out.println("please enter a valid option");
                }
            }
            catch (IndexOutOfBoundsException e){
                System.out.println("Your search is out of reach");
                break;
            }
            catch (InputMismatchException e){
                System.out.println("Not a valid input");
                break;
            }
        }

    }
}
