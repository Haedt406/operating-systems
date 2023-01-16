/*
 * this class essentially takes individual jobs to process
 */
package com.mycompany.pagingsystem;

/**
 *
 * @author haedt
 */
public class Job {
    public final int jobNumber;
    public int processed = 0;
    public final int pageReq;

    
    public Job(int jobNumber, int pageReq, int processed){
        this.jobNumber = jobNumber;
        this.processed = processed;
        this.pageReq = pageReq;
        
    }
    public void SetProcessed(){
        processed += 1;
        
    }

    public void PrintPMT(){
        System.out.println("Job Number: " + jobNumber+ " "+ "Processed: "+ processed + " out of " + pageReq);
    }
}
