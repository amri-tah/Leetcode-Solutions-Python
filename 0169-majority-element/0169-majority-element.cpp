#include <unordered_map>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> hashmap; // num, freq
        int n = nums.size();
        for (int i=0; i<n; i+=1){
            hashmap[nums[i]]++;
            if (hashmap[nums[i]]>(n/2)) return nums[i];
        }
        return -1;     
    }
};