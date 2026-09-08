class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        for(int i = 0; i < nums.size() ; i++){
            if(mp.find(nums[i]) != mp.end()){
                mp[nums[i]]++;
            }else{
                mp[nums[i]]= 1;
            }
        }


        vector<int> result;
        while(k != 0){
            int max_freq = 0;
            int max_elem = 0;
            for(auto z : mp){
                if(z.second > max_freq){
                    max_freq = z.second;
                    max_elem = z.first;
                }
            }
            result.push_back(max_elem);
            mp[max_elem] = 0;
            k--;
        }
        return result;
    }
};
