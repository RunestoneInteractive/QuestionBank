.. activecode:: completeheapcpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Trees
    :subchapter: BinaryHeapImplementation
    :topics: Trees/BinaryHeapImplementation
    :from_source: T
    :caption: The Complete Binary Heap Example C++
    :language: cpp

    #include <iostream>
    #include <vector>
    using namespace std;

    // uses a vector to creat a Binar Heap
    class BinHeap{

    private:
        vector<int> heapvector;
        int currentSize;

    public:
        // initializes the vector and an attribute currentSize
        // as 0 to allow for interger division.
        BinHeap(vector<int> heapvector){
            this->heapvector = heapvector;
            this->currentSize = 0;
        }

        // prelocates and item as far up in the
        // tree as possible to maintain
        // the Heap property
        void percUp(int i){
            while ((i / 2) > 0){
                if (this->heapvector[i] < this->heapvector[i/2]){
                    int tmp = this->heapvector[i/2];
                    this->heapvector[i/2] = this->heapvector[i];
                    this->heapvector[i] = tmp;
                }
                i = i/2;
            }

        }

        // appends item to the end of the vector
        void insert(int k){
            this->heapvector.push_back(k);
            this->currentSize = this->currentSize + 1;
            this->percUp(this->currentSize);
        }

        // prelocates and item as far up in the
        // tree as possible to maintain
        // the Heap property
        void percDown(int i){
            while ((i*2) <= this->currentSize){
                int mc = this->minChild(i);
                if (this->heapvector[i] > this->heapvector[mc]){
                    int tmp = this->heapvector[i];
                    this->heapvector[i] = this->heapvector[mc];
                    this->heapvector[mc] = tmp;
                }
                i = mc;
            }
        }

        int minChild(int i){
            if (((i*2)+1) > this->currentSize){
                return i * 2;
            }
            else{
                if (this->heapvector[i*2] < this->heapvector[(i*2)+1]){
                    return i * 2;
                }
                else{
                    return (i * 2) + 1;
                }
            }
        }

        // restores full complince with the heap structure
        // and heap order properties after the root is removed
        // by  taking the last item and moving it to the root position
        // and pushing the new root node down the tree to its proper postion.
        int delMin(){
            int retval = this->heapvector[1];
            this->heapvector[1] = this->heapvector[this->currentSize];
            this->currentSize = this->currentSize - 1;
            this->heapvector.pop_back();
            this->percDown(1);
            return retval;
        }

        void buildheap(vector<int> avector){
            int i = avector.size() / 2;
            this->currentSize = avector.size();
            this->heapvector.insert(this->heapvector.end(), avector.begin(), avector.end());
            while (i > 0){
                this->percDown(i);
                i = i - 1;
            }
        }

        bool isEmpty(){
            if (this->heapvector.size()>0){
                return false;
            }
            return true;
        }

        int findMin(){
            return this->heapvector[1];
        }
    };


    int main(){
        int arr[] = {9, 5, 6, 2, 3};
        vector<int> a(arr,arr+(sizeof(arr)/ sizeof(arr[0])));

        vector<int> vec;
        vec.push_back(0);

        BinHeap *bh = new BinHeap(vec);
        bh->buildheap(a);

        cout << bh->delMin() << endl;
        cout << bh->delMin() << endl;
        cout << bh->delMin() << endl;
        cout << bh->delMin() << endl;
        cout << bh->delMin() << endl;

        return 0;
    }