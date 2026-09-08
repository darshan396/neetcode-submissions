class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> mp;
        for(int i =0;i<strs.size();i++){
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            if(mp.find(temp) == mp.end()){
                vector<string> temp_v;
                temp_v.push_back(strs[i]);
                mp[temp] = temp_v;
            }
            else{
                mp[temp].push_back(strs[i]);
            }
        }
        for(auto z : mp){
            result.push_back(z.second);
        }
        return result;
    }
};
