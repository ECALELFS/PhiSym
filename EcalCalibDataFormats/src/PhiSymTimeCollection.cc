#include "PhiSym/EcalCalibDataFormats/interface/PhiSymTimeCollection.h"
#include "TMath.h"

//**********constructors******************************************************************
PhiSymTimeCollection::PhiSymTimeCollection()
{
}
            
//**********destructor********************************************************************
PhiSymTimeCollection::~PhiSymTimeCollection()
{}

//**********getters***********************************************************************
float PhiSymTimeCollection::GetTimeSum() const
{
   return GetTimeSum(0.0f, -1.0f);
}

float PhiSymTimeCollection::GetTimeSum2() const
{
   return GetTimeSum2(0.0f, -1.0f);
}

size_t PhiSymTimeCollection::GetTimeN() const
{
   return GetTimeN(0.0f, -1.0f);
}


const TimeCollection PhiSymTimeCollection::GetTimes(float low, float hi)    const
{
   TimeCollection ret;
   bool range = true;
   if(hi < low)
      range = false;
   auto low_comp = CompressTime(low);
   auto hi_comp = CompressTime(hi);
   for(auto t : times_)
   {
      if(!range || (t >= low_comp && t <= hi_comp))
         ret.push_back(t);
   }
   return ret;
}

float PhiSymTimeCollection::GetTimeSum(float low, float hi)  const
{
   float time = 0;
   for( auto t : GetTimes(low,hi))
   {
      time += UncompressTime(t);
   }
   return time;
}
float PhiSymTimeCollection::GetTimeSum2(float low, float hi)  const
{
   float time2 = 0;
   for( auto t : GetTimes(low,hi))
   {
      time2 += TMath::Power(UncompressTime(t),2);
   }
   return time2;
}
size_t PhiSymTimeCollection::GetTimeN(float low, float hi)    const
{
   return GetTimes(low,hi).size();
}
//**********utils*************************************************************************

void PhiSymTimeCollection::AddTime(float t)
{
   //Range of 16bit int
   if(t >= - MAX_TIME &&  t <= MAX_TIME)
      times_.push_back(CompressTime(t));
}

int16_t PhiSymTimeCollection::CompressTime(float t) const
{
   return (int16_t)TMath::Nint(t*1000);
}
float PhiSymTimeCollection::UncompressTime(int16_t t) const
{
   return float(t)/1000.0f;
}

void PhiSymTimeCollection::Reset()
{
    times_.clear();
}

float PhiSymTimeCollection::GetTimeMean() const
{
   return GetTimeMean(0.0f, -1.0f);
}

float PhiSymTimeCollection::GetTimeMean(float low, float hi) const
{
   return GetTimeSum(low,hi)/GetTimeN(low,hi);
}

float PhiSymTimeCollection::GetTimeStdDev() const
{
   return GetTimeStdDev(0.0f, -1.0f);
}

float PhiSymTimeCollection::GetTimeStdDev(float low, float hi) const
{
   float mean = GetTimeMean(low,hi);
   return TMath::Sqrt( GetTimeSum2(low,hi)/GetTimeN(low,hi) - mean*mean);
}

//**********operators*********************************************************************

PhiSymTimeCollection& PhiSymTimeCollection::operator+=(const PhiSymTimeCollection& rhs)
{
    for(auto t : rhs.GetTimes())
       this->times_.push_back(t);
    return *this;
}

std::ostream& operator<<(std::ostream& out, const PhiSymTimeCollection& obj)
{
    //---dump all the informations
    out << std::setw(20) << "number of times:" << obj.GetTimeN() << std::endl;
    out << std::endl;
    
    return out;
}

