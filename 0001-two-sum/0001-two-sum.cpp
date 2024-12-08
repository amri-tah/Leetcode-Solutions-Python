#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap; // {rem: index}
        for (int i=0; i<nums.size(); i+=1){
            int rem = target-nums[i];
            if (hashmap.count(rem)!=0) return {hashmap[rem], i};
            hashmap[nums[i]]=i;
        }
        return {};
    }

};