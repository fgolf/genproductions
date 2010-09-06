import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(1.918),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'PMAS(42,1)=250.0        ! LQ mass',
            'IMSS(21)=33             ! LUN number for SLHA File (must be 33)',
            'IMSS(22)=33             ! Read-in SLHA decay table',
            'MSEL=0                  ! (D=1) to select between full user control (0, then use MSUB) and some preprogrammed alternative',
            'MSUB(163)=1             ! g+g->LQ+LQbar',
            'MSUB(164)=1             ! q+qbar->LQ+LQbar'
        ),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring(
            'pythiaUESettings',
            'processParameters',
            'SLHAParameters'
        ),
        SLHAParameters = cms.vstring('SLHAFILE = Configuration/Generator/data/LQ_ue_beta1.0.out')
    )
)

configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.1 $'),
        name = cms.untracked.string('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/PYTHIA6_Exotica_LQ_ue_250_7TeV_eejj_cff.py,v $'),
        annotation = cms.untracked.string('default documentation string for PYTHIA6_Exotica_LQ_ue_250_7TeV_eejj_cff.py')
)