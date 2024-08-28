// https://leetcode.com/problems/top-k-frequent-elements/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if(nums.size() == 0 or nums.size() == 1){
            return nums;
        }

        unordered_map<int, int> map1; // Numero: conteo de veces que ha apareceido
        unordered_map<int, vector<int>> map2; // Numero de veces que se repite : numeros correspondientes
        vector<int> result;

        for(int i = 0; i < nums.size(); i++){
            int n, c;
            n = nums[i];
            map1[n]++;
            c = map1[n];
            map2[c].push_back(n);
        }
        
        for(int i = nums.size() - 1; i > 0; i--){
            vector<int> v = map2[i];
            for(auto x: v){
                if(find(result.begin(), result.end(), x) == result.end()){ // Verifica si x esta en result
                    result.push_back(x);
                }
                if(result.size() == k){
                    break;
                }
            }
            if(result.size() == k){
                break;
            }
        }

        return result;
    }
};

int main(){
    Solution Solucion;

    vector<int> nums = {3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6}; 
    int k = 3;

    vector<int> result = Solucion.topKFrequent(nums, k);
    for(auto x: result){
        cout << x << " ";
    }
}