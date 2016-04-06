#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "TMath.h"

//**********constructors******************************************************************
PhiSymRecHit::PhiSymRecHit():
    id_(0), nHits_(0), et2Sum_(0), lcSum_(0), lc2Sum_(0)
{
    for(int i=0; i<N_MISCALIB_VALUES; ++i)
        etSum_[i] = 0;
}
            
PhiSymRecHit::PhiSymRecHit(uint32_t id, float* etValues):
    id_(id), nHits_(0), et2Sum_(0), lcSum_(0), lc2Sum_(0)
{
    for(int i=0; i<N_MISCALIB_VALUES; ++i)
        etSum_[i] = 0;

    if(etValues)
        AddHit(etValues);
}

//**********destructor********************************************************************
PhiSymRecHit::~PhiSymRecHit()
{}

//**********getters***********************************************************************
float PhiSymRecHit::GetTimeSum() const
{
   float time = 0;
   for( auto t : times_)
      time += UncompressTime(t);
   return time;
}

float PhiSymRecHit::GetTimeSum2() const
{
   float time2 = 0;
   for( auto t : times_)
      time2 += TMath::Power(UncompressTime(t),2);
   return time2;
}

size_t PhiSymRecHit::GetTimeN() const
{
   return times_.size();
}


const PhiSymRecHit::timevec PhiSymRecHit::GetTimes(float low, float hi)    const
{
   timevec ret;
   auto low_comp = CompressTime(low);
   auto hi_comp = CompressTime(hi);
   for(auto t : times_)
   {
      if(t >= low_comp && t <= hi_comp)
         ret.push_back(t);
   }
   return ret;
}

float         PhiSymRecHit::GetTimeSum(float low, float hi)  const
{
   float time = 0;
   for( auto t : GetTimes(low,hi))
   {
      time += UncompressTime(t);
   }
   return time;
}
float         PhiSymRecHit::GetTimeSum2(float low, float hi)  const
{
   float time2 = 0;
   for( auto t : GetTimes(low,hi))
   {
      time2 += TMath::Power(UncompressTime(t),2);
   }
   return time2;
}
size_t        PhiSymRecHit::GetTimeN(float low, float hi)    const
{
   return GetTimes(low,hi).size();
}
//**********utils*************************************************************************

void PhiSymRecHit::AddHit(float* etValues, float laserCorr)
{
    if(etValues[0] > 0)
    {
        ++nHits_;
        etSum_[0] += etValues[0];
        et2Sum_ += etValues[0]*etValues[0];
        lcSum_ += laserCorr;
        lc2Sum_ += laserCorr*laserCorr;
    }
    for(short i=1; i<N_MISCALIB_VALUES; ++i)        
        etSum_[i] += etValues[i];
}

void PhiSymRecHit::AddTime(float t)
{
   //Range of 16bit int
   if(t >= -32.678 &&  t <= 32.767)
      times_.push_back(CompressTime(t));
}

int16_t PhiSymRecHit::CompressTime(float t) const
{
   return (int16_t)TMath::Nint(t*1000);
}
float PhiSymRecHit::UncompressTime(int16_t t) const
{
   return float(t)/1000.0f;
}

void PhiSymRecHit::Reset()
{
    nHits_ = 0;
    et2Sum_ = 0;
    lcSum_ = 0;
    lc2Sum_ = 0;
    for(short i=0; i<N_MISCALIB_VALUES; ++i)
        etSum_[i] = 0;
    times_.clear();
}

//**********operators*********************************************************************

PhiSymRecHit& PhiSymRecHit::operator+=(const PhiSymRecHit& rhs)
{
    if(id_ == 0)
        id_ = rhs.GetRawId();
    nHits_ += rhs.GetNhits();
    et2Sum_ += rhs.GetSumEt2();
    lcSum_ += rhs.GetLCSum();
    lc2Sum_ += rhs.GetLC2Sum();
    for(short i=0; i<N_MISCALIB_VALUES; ++i)
        etSum_[i] += rhs.GetSumEt(i);

    for(auto t : rhs.GetTimes())
       this->times_.push_back(t);
    return *this;
}

std::ostream& operator<<(std::ostream& out, const PhiSymRecHit& obj)
{
    //---dump all the informations
    out << std::endl;
    out << std::setw(20) << "raw-id:" << obj.GetRawId() << std::endl;
    out << std::setw(20) << "number of hits:" << obj.GetNhits() << std::endl;
    for(short i=1; i<N_MISCALIB_VALUES; ++i)        
        out << std::setw(20) << "sumEt: " << i << obj.GetSumEt(i) << std::endl;
    out << std::setw(20) << "sumEt2: " << obj.GetSumEt2() << std::endl;
    out << std::setw(20) << "laser-corr sum: " << obj.GetLCSum() << std::endl;
    out << std::setw(20) << "laser-corr^2 sum: " << obj.GetLC2Sum() << std::endl;
    out << std::endl;
    
    return out;
}
