import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    int[] heap = new int[100000];
    int heap_size;

    public static void insertHeap(Main h, int item){
        h.heap_size = h.heap_size + 1;
        int i = h.heap_size;
        while((i!=1)&&(item > h.heap[i / 2])){
            h.heap[i] = h.heap[i /2];
            i /= 2;
        }
        h.heap[i] = item;
    }

    public static int deleteHeap(Main h){
        int parent, child;
        int item, temp;
        item = h.heap[1];
        temp = h.heap[h.heap_size];
        h.heap_size = h.heap_size - 1;
        parent = 1;
        child = 2;
        while(child <= h.heap_size){
            if((child < h.heap_size) && (h.heap[child]) < h.heap[child +1]){
                child++;
            }
            if(temp >= h.heap[child]){
                break;
            }
            else{
                h.heap[parent] = h.heap[child];
                parent = child;
                child = child * 2;
            }
        }
        h.heap[parent] = temp;
        return item;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int item;
        Main heap = new Main();
        int n = Integer.parseInt(br.readLine());


        for(int i = 0; i<n; i++){
            int x = Integer.parseInt(br.readLine());
            if( x == 0){
                int size = heap.heap_size;
                if(size != 0) {
                    item = Main.deleteHeap(heap);
                    System.out.println(item);
                } else{
                    System.out.println(0);
                }
            } else{
                Main.insertHeap(heap, x);
            }
        }
    }
}