/**
 * This program creates a double linked list, 4 threads, 2 for producers, one odd and one even, and 2 consumers, one odd and one even.
 * each thread has to access the linked list and we use mutex to make sure each one can access it properly.
 * the consumers remove from the head of the DLL and the producers add to the end of the DLL
 * @author haedt
 */
#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include <mutex>
#include <pthread.h>

pthread_mutex_t lock;
pthread_cond_t count_threshold_cv;
//pthread_t tid[3];
int counter = 0;
struct node{int key; node *next;node *prev;};
class linkedList{
    node*head;
    node*tail;
public:
    linkedList() {head =NULL;tail=NULL;}
    void addNode(int);
    void deleteNode();
    void display();
    int checkHead(int);
};
int linkedList::checkHead(int num){
    if(num ==1 && head->key%2!=0){
        return 0;
    }
    else if (num ==1 && head->key%2!=0){
        return 1;
    }
    if(num ==2 && head->key%2==0){
        return 0;
    }
    else{
        return 1;
    }
}
void linkedList::deleteNode() {
    if (head == NULL) {
        std::cout << " Nothing to delete in LL \n";
        return;
    }
    else {
        node *temp = head;
        temp=temp->next;
        head = temp;
        temp->prev = NULL;
    /*    node *temp = head;
        node*temp2;
        if (num == 2) {
            while (temp->key % 2 != 0) {
                temp = temp->next;
            }
            if(temp->prev==NULL) {
                temp=temp->next;
                head = temp;
                temp->prev = NULL;
            }
            else{
                temp2=temp;
                temp=temp->prev;
                temp2=temp2->next;
                temp2->prev=temp;
                temp->next=temp2;
            }
        }
        if (num == 1) {
            while (temp->key % 2 == 0) {
                temp = temp->next;
            }
            if(temp->prev==NULL) {
                temp=temp->next;
                head = temp;
                temp->prev = NULL;
            }
            else{
                temp2=temp;
                temp=temp->prev;
                temp2=temp2->next;
                temp2->prev=temp;
                temp->next=temp2;
            }
        }*/
    }
}
void linkedList::addNode(int num) {
    node *newNode = new node();
    newNode->key=num;
    if(head == NULL){
        head = newNode;
        tail = newNode;
        head->prev=NULL;
        tail->prev=NULL;
    }
    else{
        tail->next=newNode;
        newNode->prev=tail;
        tail=newNode;
        tail->next=NULL;
    }
}
linkedList list;
void linkedList::display(){
    node* temp = head;
   // std::cout<<"List: ";

    if (head!=NULL){
        std::cout<<" "<<head->key<<" ";
        temp = temp->next;
        while(temp != NULL){
            std::cout<<temp->key<<" ";
            temp=temp->next;
        }
        std::cout<<"\n";
        return;
    }
    else{
        std::cout<<"List is Empty";
    }
}

int Num = rand() % 50;
void *producerOdd(void *arg){                                           //producer odd is almost the same as even
    while(true) {                                                       //while true allows it to run forever
        pthread_mutex_lock(&lock);
        if (counter >= 30) {                                                //if nodes in the LL is over or = 30 then stop making more
            std::cout << " Producer Odd tried to add to linked list, but length limit reached \n";
            sleep(1);
        }
        else {                                                              //creates a node at the end of the LL
            std::srand(std::time(nullptr));
            Num = rand() % 50;
            while (Num % 2 == 0) {
                Num = rand() % 50;
            }
            list.addNode(Num);
            std::cout<<"Producer Odd added to LL: ";
            list.display();
            counter++;
            pthread_mutex_unlock(&lock);
            sleep(1);

        }
    }
}
void *producerEven(void *arg){
    while(true) {
        pthread_mutex_lock(&lock);
        if (counter >= 30) {
            std::cout << " Producer Even tried to add to linked list, but length limit reached \n";
            sleep(1);
        }
        else {
            std::srand(std::time(nullptr));
            Num = rand() % 50;
            while (Num % 2 != 0) {
                Num = rand() % 50;
            }
            list.addNode(Num);
            std::cout<<"Producer Even added to LL: ";
            list.display();
            counter++;
            pthread_mutex_unlock(&lock);
            sleep(1);
        }
    }
}
void *consumerEven(void *arg){
    while(true) {
        pthread_mutex_lock(&lock);
        if (counter <= 0) {
        //    pthread_cond_signal(&count_threshold_cv);
            std::cout << " Consumer Even could not delete from LL, \n";
            sleep(1);
        }
        if (list.checkHead(2)==1){
            pthread_mutex_unlock(&lock);
            sleep(1);
        }
        else {
            list.deleteNode();
            std::cout<<"Consumer Even deleted from LL: ";
            list.display();
            counter--;
            pthread_mutex_unlock(&lock);
            sleep(1);
        }
    }
}
void *consumerOdd(void *arg){                                       //our consumer thread for odd, consumer even is close to the same
    while(true) {
        pthread_mutex_lock(&lock);                                  //locks the thread and then uses it when it gets a chance
        if (counter <= 0) {
       //     pthread_cond_signal(&count_threshold_cv);
            std::cout << " Consumer Odd could not delete from LL \n";
            sleep(1);
        }
        if (list.checkHead(1)==1){                             //checks the head node and if it isnt odd then unlocks and sleeps
            pthread_mutex_unlock(&lock);
            sleep(1);
        }
        else {                                                      //deletes the head node then unlocks
            list.deleteNode();
            std::cout<<"Consumer Odd deleted from LL: ";
            list.display();
            counter--;
            pthread_mutex_unlock(&lock);
            sleep(1);
        }
    }
}
int main() {
        pthread_t pe, po, ce,co;                                            //gets our threads ready for creation by declaring them
        pthread_mutex_init(&lock, NULL);                                    //sets up our lock
        pthread_attr_t attr;                                                //attribute for our lock
        std::srand(std::time(nullptr));                           //generate a "random" number based on the time it pulls
        list.addNode(3);                                                //adds a node with the key "1"
        list.addNode(1);
        list.addNode(7);
        counter = counter +3;
        pthread_attr_init(&attr);                                               //sets an attribute for the thread
     //   pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);         //allows the threads to be in a joinable or detached state
        pthread_create(&pe, &attr, producerEven, NULL);                      //start actually creating our threads
      //  pthread_join(pe,NULL);
        pthread_create(&po, &attr, producerOdd, NULL);
    //    pthread_join(po,NULL);
        pthread_create(&co, &attr, consumerOdd, NULL);
    //    pthread_join(co,NULL);
        pthread_create(&ce, &attr, consumerEven, NULL);
    //    pthread_join(ce,NULL);
    int t =0;
    while(t != 25){
            sleep(1);
        //    std::cout<<counter;
        t++;
    }
        pthread_cancel(ce);                                               //closes the treads
        pthread_cancel(co);
        pthread_cancel(pe);
        pthread_cancel(po);
        pthread_attr_destroy(&attr);                                        //destroys the attribute for the threads
        pthread_mutex_destroy(&lock);                                       //destroys the mutex
        pthread_cond_destroy((&count_threshold_cv));
        return 0;
}