class Solution {
public:
    int maxArea(vector<int>& height) {
             int area=0;
        int start=0;
        int end=height.size()-1;
      while(start!=end){
          
    int cur_area=min(height.at(start), height.at(end) )*(end-start);
          area=max(area,cur_area);
        //  if(area%(end-start)>max(height)) break;
        
          height[start] <= height[end] ? start ++ : end--; 
      }
           
           
       
        return area;
    }
};