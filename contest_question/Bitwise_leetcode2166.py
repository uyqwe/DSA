class Bitset:
    
    def __init__(self, size: int):
        self.bitsize=[0]*size
        self.size=size
        self.flp=False
        self.cnt=0
        

    def fix(self, idx: int) -> None:
        if self.flp==False:
            if self.bitsize[idx]==0:
                self.bitsize[idx]=1
                self.cnt+=1
        else:
            if self.bitsize[idx]==1:
                self.bitsize[idx]=0
                self.cnt+=1
                
        #print(self.cnt)

    def unfix(self, idx: int) -> None:
        if self.flp==False:
            if self.bitsize[idx]==1:
                self.bitsize[idx]=0
                self.cnt-=1
        else:
            if self.bitsize[idx]==0:
                self.bitsize[idx]=1
                self.cnt-=1
        #print(self.cnt)
        

    def flip(self) -> None:
        if self.flp==False:
            self.flp=True
        else:
            self.flp=False
        self.cnt=self.size-self.cnt
        #print(self.cnt)
        

    def all(self) -> bool:
        #print(self.cnt)
        return self.cnt>=self.size
       
        

    def one(self) -> bool:
        #print(self.cnt)
        return self.cnt>=1
        
        

    def count(self) -> int:
        count1=self.cnt
        #print("count=",count1)
        return count1
        

    def toString(self) -> str:
        if self.flp==False:
            ans=''
            for i in self.bitsize:
                ans=ans+str(i)
            return ans
        else:
            ans=''
            for i in self.bitsize:
                if i==0:
                    ans=ans+str(1)
                else:
                    ans=ans+str(0)
            return ans


        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()