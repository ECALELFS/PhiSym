#ifndef DATAFORMAT_PHISYMTIMECOLLECTION_H
#define DATAFORMAT_PHISYMTIMECOLLECTION_H

/** \class PhiSymTimeCollection
 * 
 * Dataformat dedicated to Phi Symmetry ecal time calibration
 * 
 */

#include <iostream>
#include <iomanip>
#include <vector>

//---define the number of allowed mis-calibrated values for etSum_ (+ the central value)
#define MAX_TIME 32.767

typedef std::vector<int16_t> TimeCollection;

class PhiSymTimeCollection
{
public:
    //---ctors---
    PhiSymTimeCollection();
    
    //---dtor---
    ~PhiSymTimeCollection();

    //---getters---
    inline const TimeCollection GetTimes()      const {return times_;};
    float           GetTimeSum()         const;
    float           GetTimeSum2()         const;
    size_t          GetTimeN()           const;
    float           GetTimeMean()         const;
    float           GetTimeStdDev()         const;
    //---getters for time in range---
    const TimeCollection GetTimes(float low, float hi)    const;
    float         GetTimeMean(float low, float hi) const;
    float         GetTimeSum(float low, float hi)  const;
    float         GetTimeSum2(float low, float hi)  const;
    size_t        GetTimeN(float low, float hi)    const;
    float         GetTimeStdDev(float low, float hi) const;

    //---utils---
    void         AddTime(float t);
    int16_t      CompressTime(float t) const;
    float        UncompressTime(int16_t t) const;
    void         Reset();

    //---operators---
    PhiSymTimeCollection& operator+=(const PhiSymTimeCollection& rhs);
    friend std::ostream& operator<<(std::ostream& out, const PhiSymTimeCollection& obj);

private:

    TimeCollection  times_;

};


#endif

