package priority_inversion;
import java.util.Scanner;
/**
 * @author haedt406
 */
public class priority_inversion{
    static void printCurrentJob(int jobNumber, job[] jobQ) {
    switch (jobNumber) {
        case 1 -> System.out.print("T1 Complete\n");
        case 2 -> {
            System.out.print("T2 ");
            if (jobQ[0].hasBeenInterupted == 1){
               for (int i = 0; i<jobQ[0].interupt;i++){System.out.print("I");}} 
            else{
            for (int i = 0; i<jobQ[0].normal;i++){
                System.out.print("N");}}
            System.out.print(" T2\n");}
        case 3 -> {
            System.out.print("T3 ");
            if (jobQ[0].hasBeenInterupted == 1){
               for (int i = 0; i<jobQ[0].interupt;i++){System.out.print("I");}} 
            else{
            for (int i = 0; i<jobQ[0].normal;i++){
                System.out.print("N");}}
            System.out.print(" T3\n");}}}
public static void main(String[] args)
{
    Scanner console = new Scanner(System.in);
    int jobs[][] = {{1,3},{3,2},{6,3},{8,1},{10,2},{12,3},{26,1}};
    int test[][] = {{1,1},{3,2},{6,3}};
    int menu = 0;
    int read0 = 0;
    int read1 = 0;
    job[] buffer = new job[1];
    buffer[0] = new job(0, 0, false, 0);
    int jobQLength = 0;
    int has = 0;
    while ( menu != 3){
        System.out.println("This program is to demonstrate priority inversion. The time to run one slice is asked every iteration\n" );
//        System.out.println( "Enter 1 to run jobs {{1,1},{3,2},{6,3}}, these are test jobs\n");
        System.out.println("Enter 1 to run jobs {{1,3},{3,2},{6,3},{8,1},{10,2},{12,3},{26,1}}, these are the main jobs to test with priority inversion\n" );
        System.out.println( "Enter 3 to exit the program: ");
        menu = console.nextInt();
        if (menu == 1){
            int run1 = 0;
            job[] jobQ = new job[7];
            while (true){
                OUTRUNPROCESSONESLICE:
                if(jobQ[0] == null){
                    break OUTRUNPROCESSONESLICE;} 
                else {
                    if(jobQ[0] != null){
                        jobQ[0].setProcessed();
                        if (jobQ[0].toProcess ==0){
                            if(jobQ[0].jobNumber == 1 || jobQ[0].jobNumber ==3){
                                buffer[0].hasBuffer=0;
                                has = 1;}
                            System.out.print("time " +run1 + ", ");
                            printCurrentJob(jobQ[0].jobNumber, jobQ);
                            for (int j = 1; j<jobQLength;j++){
                                jobQ[j-1] = jobQ[j];
                                jobQ[j] = null;}
                            jobQLength--;
                            if(jobQLength ==0){
                                jobQ[0] = null;}
                            if(has ==1){
                            SETNEWJOBBUFFERBREAK:
                            for (int i = 0; i <jobQLength;i++){
                                if(jobQ[i].jobNumber == 1){
                                    buffer[0] = jobQ[i];jobQ[i].setBuffer(1);System.out.println("T1 111 T1");buffer[0].hasBuffer=1;break SETNEWJOBBUFFERBREAK;}
                                else if (jobQ[i].jobNumber == 3){
                                    buffer[0] = jobQ[i];jobQ[i].setBuffer(1);System.out.println("T3 333 T3"); buffer[0].hasBuffer=3; break SETNEWJOBBUFFERBREAK;}
                            }}
                            has =0;}
                }}
                
            OUTADDTOQUEUE:
                for (int row = 0; row < 7; row++) {
                    for (int column = 0; column < 2; column++) {
                        if (column == 0){read0 = jobs[row][column];}
                        else if (column ==1){read1 = jobs[row][column];}}
                    if (read0 == run1){
                        if(read1 ==1) {jobQ[jobQLength] = new job(read1, 1, false, 1);
                            if(buffer[0].hasBuffer == 0){buffer[0] = jobQ[jobQLength];jobQ[jobQLength].setBuffer(1);System.out.println("T1 111 T1");buffer[0].hasBuffer=1;}
                            else if (buffer[0].hasBuffer==3){
                                for(int JQL = jobQLength; JQL >= 0;JQL--)
                                {if (jobQ[JQL].hasBuffer ==3){
                                    System.out.println("PRIORITY INVERSION");
                                    jobQ[JQL].priority = 1;
                                }}}
                            jobQLength++; break OUTADDTOQUEUE;}
                        if(read1 ==2) {jobQ[jobQLength] = new job(read1, 2, false, 10);jobQLength++; break OUTADDTOQUEUE;}
                        if(read1 ==3) {jobQ[jobQLength] = new job(read1, 3, false, 1);
                        if(buffer[0].hasBuffer == 0){buffer[0] = jobQ[jobQLength];jobQ[jobQLength].setBuffer(1);System.out.println("T3 333 T3"); buffer[0].hasBuffer=3;}
                                           jobQLength++;  break OUTADDTOQUEUE;}
                    }}

                for(int PSLoop = jobQLength; PSLoop>0; PSLoop--){
                    if(jobQ[PSLoop] != null && jobQ[PSLoop-1]!=null){
                        for(int in = PSLoop; in >0;in--){
                            if (in == 1 && jobQ[in].priority < jobQ[in-1].priority){
                                System.out.print("time " +run1 + ", ");
                                printCurrentJob(jobQ[in-1].jobNumber, jobQ);}
                            if(jobQ[in].priority < jobQ[in-1].priority){
                                job temp = new job(0, 0, false, 0);
    //                            System.out.println("Swapped jobs "+ jobQ[in].jobNumber + " and " + jobQ[in-1].jobNumber + " on in = " + in);
                                if(jobQ[in-1].jobNumber == 2 || jobQ[in-1].jobNumber == 3 && (in-1) == 0){
                                    jobQ[in-1].sethasBeenInterupted();}
                                temp = jobQ[in];
                                jobQ[in] = jobQ[in-1];
                                jobQ[in-1]=temp; 
                                in=jobQLength;}}
                }}
                
                System.out.println("Current run time: " + run1);
                System.out.print("Queue for jobs: \n");
                for (job jobQ1 : jobQ) {
                    if (jobQ1 == null) {System.out.print("| empty |\n");} 
                    else {jobQ1.printJob();}}
                System.out.print( "\nEnter 1 to increment time by 1 or 9 to exit this iteration of priority inversion: ");
                menu = console.nextInt();
                if(menu == 9){break;}
                run1++;
                if (run1 >=30){
                    System.out.println("No more jobs to process"); menu =9;}
                if(jobQ[0] != null){
                if(jobQ[0].hasBeenInterupted ==0 &&jobQ[0].jobNumber ==2 || jobQ[0].jobNumber == 3 ){jobQ[0].normal++;}
                else if(jobQ[0].hasBeenInterupted ==1&&jobQ[0].jobNumber ==2 || jobQ[0].jobNumber == 3){jobQ[0].interupt++;}}
            }   
        }
    }
}}