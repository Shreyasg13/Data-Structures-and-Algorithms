class Solution {
public:
    int maxProfit(vector<int>& prices) {
         
        int Max=INT_MIN;
        int Min=INT_MAX;
        for(int i=0;i<prices.size();i++)
        {
           
            Min=min(Min,prices[i]);
            Max=max(Max,prices[i]-Min);  
        }
        return Max;
    }
};