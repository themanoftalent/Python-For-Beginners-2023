#include <iostream>
using namespace std;

// Stack node structure
struct StackNode {
int data;

StackNode* next;

};

// Stack class
class Stack {
private:
StackNode* top;

public:
Stack() {
top = NULL;
}


// Adds an element to the stack
void push(int x) {
    StackNode* newNode = new StackNode(); // Create new node
    newNode->data = x;                    // Set data to new node
    newNode->next = top;                  // New node points to current top
    top = newNode;                        // Update top to new node
}

// Removes an element from the stack
int pop() {
    if (top == NULL) {
        cout << "Stack is empty" << endl;
        return -1;
    }
    int data = top->data;                // Get data from top node
    StackNode* temp = top;               // Temporary node
    top = top->next;                     // Move top to next node
    delete temp;                         // Delete old top node
    return data;                         // Return the removed data
}

bool isEmpty() {
    return top == NULL;
}


};

// Queue node structure
struct QueueNode {
int data;

QueueNode* next;

};

// Queue class
class Queue {
private:
QueueNode *front, *rear; // Pointers to the front and rear

public:
Queue() {
front = rear = NULL;
}

// Adds an element to the queue
void enqueue(int x) {
    QueueNode* newNode = new QueueNode(); // Create new node
    newNode->data = x;                    // Set data to new node
    newNode->next = NULL;                 // New node is the last

    if (rear == NULL) {
        front = rear = newNode;
        return;
    }

    // Add new node at the rear and update rear
    rear->next = newNode;
    rear = newNode;
}

// Removes an element from the queue
int dequeue() {
    if (front == NULL) {
        cout << "Queue is empty" << endl;
        return -1;
    }
    int data = front->data;               // Get data from front node
    QueueNode* temp = front;              // Temporary node
    front = front->next;                  // Move front to next node

    if (front == NULL) rear = NULL;

    delete temp;                          // Delete old front node
    return data;                          // Return the removed data
}

// Checks if the queue is empty
bool isEmpty() {
    return front == NULL;
}


};

// Function to transfer elements from Queue to Stack
Stack transferQueueToStack(Queue& q) {
Stack s;
while (!q.isEmpty()) {
s.push(q.dequeue());
}
return s;
}

// Main method
int main() {
Queue q;
// Enqueue elements into the queue
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);

// Transfer elements from queue to stack
Stack s = transferQueueToStack(q);

// Print elements from the stack
while (!s.isEmpty()) {
    cout << s.pop() << " ";
}

return 0;