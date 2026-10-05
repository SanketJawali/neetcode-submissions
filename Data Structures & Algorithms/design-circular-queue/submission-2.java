class MyCircularQueue {
    private int[] queue;
    private int front;
    private int rear;
    private int size;
    private int k;

    public MyCircularQueue(int k) {
        this.queue = new int[k];
        this.front = 0;
        this.rear = k - 1;  // points to end, incremented when enqueued
        this.size = 0;
        this.k = k;
    }
    
    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        rear = (rear + 1) % k;
        queue[rear] = value;
        size++;
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }

        queue[front] = -1;    // Remove element
        front = (front + 1) % k;
        size--;
        return true;
    }
    
    public int Front() {
        return !isEmpty() ? queue[front] : -1;
    }
    
    public int Rear() {
        return !isEmpty() ? queue[rear] : -1;
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    public boolean isFull() {
        return size == k;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */