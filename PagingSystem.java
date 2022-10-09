/**
 *
 * @author haedt
 */

package com.mycompany.pagingsystem;
import java.util.Scanner;


public class PagingSystem{
    

public static void main(String[] args)  {
    int menuNumber = 0;
    Job[] PMT = new Job[16];                                                    //creates an array of objects Job
    Scanner console = new Scanner(System.in);
    int jobNumber;
    int bytes;
    int toDelete;
    int currentJob = 1;
        while (menuNumber != 5){                                                //our menu system for the paging table
                System.out.println("Enter 1 to put in a new job in the format: job_number bytes, example, 1 30000");
                System.out.println("Enter 2 to delete a specific job: job_number 0, example, to delete job 2 the first entry is 2 and the second entry is 0");
                System.out.println("Enter 3 to print to print the current memory status");
                System.out.println("Enter 5 to exit");
            int switchHasJob = 0;
            int switchEmptyTable =16;
            for (int i = 0; i <16;i++){                                         //this is our "timer" that automatically goes through our memory table each cycle of the menu and the current job it completes 1 frame, doesnt unload the job until each frame has been processed
                if (PMT[i] == null){
                    switchEmptyTable--;
                    continue;
                }
                if (PMT[i].jobNumber == currentJob){
                    PMT[i].SetProcessed();
                    switchHasJob =1;
                    if (PMT[i].processed == PMT[i].pageReq){
                        for (int j = 0; j <16;j++){
                        if (PMT[j] == null){
                            continue;
                        }
                            if (PMT[j].jobNumber == currentJob){
                                PMT[j] = null;
                            }
                        }
                        System.out.println("Job: " + currentJob + " has been processed.");
                        currentJob++;
                    }
                } 
            }
            if (switchHasJob != 1 && switchEmptyTable !=0){
                    currentJob++;
            }
            menuNumber = console.nextInt();
            switch(menuNumber){
                
                case 1 -> {
                    System.out.println("Enter Job Number: ");
                    jobNumber = console.nextInt();
                    System.out.println("Enter Number of Bytes: ");
                    bytes = console.nextInt();
                    if (bytes == 0){return;}
                    int pageReq;
                    if (bytes % 4096 ==0){pageReq = bytes/4096;}
                    else{pageReq = 1+ (bytes / 4096);}
                    int internalPageReq = pageReq;
                    for (int i = 0; i<16;i++){
                        if (internalPageReq > 0){
                        if (PMT[i] == null){
                        PMT[i] = new Job(jobNumber,pageReq, 0);
                        System.out.print("Position inserted into Memory[ "+ i + " ]");
                        PMT[i].PrintPMT();
                        internalPageReq -= 1;
                        if (internalPageReq ==0){
                            break;
                        }
                        }                           
                        }
                    }
                    System.out.print("Job: " + jobNumber + " inserted into memory");
                    System.out.println();
                    break;
            }
                case 2 -> {
                    System.out.println("Enter Job Number to delete: ");
                    toDelete = console.nextInt();
                    for (int i = 0; i<16;i++){
                        if (PMT[i] == null){
                            continue;
                        }
                        else if (PMT[i].jobNumber == toDelete){
                            PMT[i] = null;
                        }
                        }
                    break;
                    }
                case 3 -> {
                    for (int i = 0; i<16;i++){
                        System.out.print("Position in Memory[ "+ i + " ] ");
                        if (PMT[i] == null){
                            System.out.println(" Nothing loaded into this frame");
                        }
                        else{
                        PMT[i].PrintPMT();
                    }
                    }
                    break;
                }
                case 5 -> {
                    menuNumber = 5; 
                break;
        }
        }     
}
}
}
