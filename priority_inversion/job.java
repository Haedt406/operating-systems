package priority_inversion;
/**
 *
 * @author haedt
 */
public class job {
    public final int jobNumber;
    public int toProcess = 0;
    public int priority;
    public boolean mutex;
    public int normal;
    public int interupt;
    public int hasBeenInterupted;
    public int hasBuffer;
    public job(int jobNumber, int priority, boolean mutex, int toProcess){
        this.jobNumber = jobNumber;
        this.toProcess = toProcess;
        this.priority = priority;
        this.mutex = mutex;
        this.normal = 0;
        this.hasBeenInterupted = 0;
        this.hasBuffer =0;
        this.interupt = 0;}
    public void setProcessed(){toProcess -= 1;}
    public void setPriority(int priority){this.priority = priority;}
    public void sethasBeenInterupted(){this.hasBeenInterupted=1;}
    public void setBuffer(int buffer){this.hasBuffer =buffer;}
    public void printJob(){System.out.print(" Job Number: " + jobNumber+ " "+ "Progress: "+ toProcess + " priority " + priority + " | \n");}
}
