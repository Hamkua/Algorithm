import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] heap = new int[100001];
    static int heap_size;

    public static void insertHeap(int item){
        heap_size = heap_size + 1;
        int i = heap_size;
        while((i!=1)&&(item < heap[i / 2])){
            heap[i] = heap[i /2];
            i /= 2;
        }
        heap[i] = item;
    }

    public static int deleteHeap(){
        int parent, child;
        int item, temp;
        item = heap[1];
        temp = heap[heap_size];
        heap_size = heap_size - 1;
        parent = 1;
        child = 2;
        while(child <= heap_size){
            if((child < heap_size) && (heap[child]) > heap[child +1]){
                child++;
            }
            if(temp <= heap[child]){
                break;
            }
            else{
                heap[parent] = heap[child];
                parent = child;
                child = child * 2;
            }
        }
        heap[parent] = temp;
        return item;
    }
    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i<n; i++){
            int x = Integer.parseInt(br.readLine());
            if(x == 0) {
                if(heap_size == 0){
                    System.out.println(0);
                    continue;
                }
                int r = deleteHeap();
                System.out.println(r);
            } else{
                insertHeap(x);
            }
        }
        br.close();
    }
}