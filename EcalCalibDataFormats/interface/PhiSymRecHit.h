#ifndef DATAFORMAT_PHISYMRECHIT_H
#define DATAFORMAT_PHISYMRECHIT_H

/** \class PhiSymRecHit
 * 
 * Dataformat dedicated to Phi Symmetry ecal calibration
 * 
 * Note: SumEt array ordering:
 *       0         - central value
 *       1<->N/2   - misCalib<1
 *       N/2+1<->N - misCalib>1
 */

#include <iostream>
#include <iomanip>
#include <vector>

#include "DataFormats/DetId/interface/DetId.h"

//---define the number of allowed mis-calibrated values for etSum_ (+ the central value)
#define N_MISCALIB_VALUES 11

class PhiSymRecHit
{
public:
    typedef std::vector<int16_t> timevec;

    //---ctors---
    PhiSymRecHit();
    PhiSymRecHit(uint32_t id, float* etValues=NULL);
    
    //---dtor---
    ~PhiSymRecHit();

    //---getters---
    inline uint32_t GetRawId()           const {return id_;};
    inline uint32_t GetNhits()           const {return nHits_;};
    inline float    GetSumEt(int iMis=0) const {return etSum_[iMis];};
    inline float    GetSumEt2()          const {return et2Sum_;};
    inline float    GetLCSum()           const {return lcSum_;};
    inline float    GetLC2Sum()          const {return lc2Sum_;};
    //---getters for time---
    inline const timevec GetTimes()      const {return times_;};
    float           GetTimeSum()         const;
    float           GetTimeSum2()         const;
    size_t          GetTimeN()           const;
    //---getters for time in range---
    const timevec GetTimes(float low, float hi)    const;
    float         GetTimeSum(float low, float hi)  const;
    float         GetTimeSum2(float low, float hi)  const;
    size_t        GetTimeN(float low, float hi)    const;

    //---utils---
    void         AddHit(float* etValues, float laserCorr=0);
    void         AddTime(float t);
    int16_t      CompressTime(float t) const;
    float        UncompressTime(int16_t t) const;
    void         Reset();

    //---operators---
    PhiSymRecHit&        operator+=(const PhiSymRecHit& rhs);
    friend std::ostream& operator<<(std::ostream& out, const PhiSymRecHit& obj);

private:

    uint32_t id_;
    uint32_t nHits_;
    float    etSum_[N_MISCALIB_VALUES];
    float    et2Sum_;
    float    lcSum_;
    float    lc2Sum_;
    timevec  times_;

};

typedef std::vector<PhiSymRecHit> PhiSymRecHitCollection;

#endif
