class MinStack {
public:
    vector<int> st;

    MinStack() {

    }
    
    void push(int val) {
        st.push_back(val);

    }
    
    void pop() {
        int n = st.size()-1;
        st.erase(st.begin()+n);
    }
    
    int top() {
        return st[st.size()-1];
    }
    
    int getMin() {
        int min = INT_MAX;
        for ( int i =0;i<st.size();i++){
            if(st[i]<min){
                min = st[i];
            }
        }
        return min;
    }
};
