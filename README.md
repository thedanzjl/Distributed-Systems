# Distributed-Systems

## lab9 report

### Output of rs.status() before shutdown of primary mongodb instance (node with id=0 is PRIMARY): 


rs0:PRIMARY> rs.status()\
{\
	"set" : "rs0",\
	"date" : ISODate("2019-10-30T15:18:15.934Z"),\
	"myState" : 1,\
	"term" : NumberLong(1),\
	"syncingTo" : "",\
	"syncSourceHost" : "",\
	"syncSourceId" : -1,\
	"heartbeatIntervalMillis" : NumberLong(2000),\
	"majorityVoteCount" : 2,\
	"writeMajorityCount" : 2,\
	"optimes" : {\
		"lastCommittedOpTime" : {\
			"ts" : Timestamp(1572448687, 1),\
			"t" : NumberLong(1)\
		},\\
		"lastCommittedWallTime" : ISODate("2019-10-30T15:18:07.475Z"),\
		"readConcernMajorityOpTime" : {\
			"ts" : Timestamp(1572448687, 1),\
			"t" : NumberLong(1)\
		},\
		"readConcernMajorityWallTime" : ISODate("2019-10-30T15:18:07.475Z"),\
		"appliedOpTime" : {\
			"ts" : Timestamp(1572448687, 1),\
			"t" : NumberLong(1)\
		},\
		"durableOpTime" : {\
			"ts" : Timestamp(1572448687, 1),\
			"t" : NumberLong(1)\
		},\
		"lastAppliedWallTime" : ISODate("2019-10-30T15:18:07.475Z"),\
		"lastDurableWallTime" : ISODate("2019-10-30T15:18:07.475Z")\
	},\
	"lastStableRecoveryTimestamp" : Timestamp(1572448667, 1),\
	"lastStableCheckpointTimestamp" : Timestamp(1572448667, 1),\
	"electionCandidateMetrics" : {\
		"lastElectionReason" : "electionTimeout",\
		"lastElectionDate" : ISODate("2019-10-29T17:36:04.570Z"),\
		"termAtElection" : NumberLong(1),\
		"lastCommittedOpTimeAtElection" : {\
			"ts" : Timestamp(0, 0),\
			"t" : NumberLong(-1)\
		},\
		"lastSeenOpTimeAtElection" : {\
			"ts" : Timestamp(1572370564, 1),\
			"t" : NumberLong(-1)\
		},\
		"numVotesNeeded" : 1,\
		"priorityAtElection" : 1,\
		"electionTimeoutMillis" : NumberLong(10000),\
		"newTermStartDate" : ISODate("2019-10-29T17:36:05.614Z"),\
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-29T17:36:05.659Z")\
	},\
	"members" : [\
		{\
			"_id" : 0,\
			"name" : "172.31.34.245:27017",\
			"ip" : "172.31.34.245",\
			"health" : 1,\
			"state" : 1,\
			"stateStr" : "PRIMARY",\
			"uptime" : 79809,\
			"optime" : {\
				"ts" : Timestamp(1572448687, 1),\
				"t" : NumberLong(1)\
			},\
			"optimeDate" : ISODate("2019-10-30T15:18:07Z"),\
			"syncingTo" : "",\
			"syncSourceHost" : "",\
			"syncSourceId" : -1,\
			"infoMessage" : "",\
			"electionTime" : Timestamp(1572370564, 2),\
			"electionDate" : ISODate("2019-10-29T17:36:04Z"),\
			"configVersion" : 3,\
			"self" : true,\
			"lastHeartbeatMessage" : ""\
		},\
		{\
			"_id" : 1,\
			"name" : "node2:27017",\
			"ip" : "172.31.34.52",\
			"health" : 1,\
			"state" : 2,\
			"stateStr" : "SECONDARY",\
			"uptime" : 77897,\
			"optime" : {\
				"ts" : Timestamp(1572448687, 1),\
				"t" : NumberLong(1)\
			},\
			"optimeDurable" : {\
				"ts" : Timestamp(1572448687, 1),\
				"t" : NumberLong(1)\
			},\
			"optimeDate" : ISODate("2019-10-30T15:18:07Z"),\
			"optimeDurableDate" : ISODate("2019-10-30T15:18:07Z"),\
			"lastHeartbeat" : ISODate("2019-10-30T15:18:14.154Z"),\
			"lastHeartbeatRecv" : \("2019-10-30T15:18:14.154Z"),\
			"pingMs" : NumberLong(0),\
			"lastHeartbeatMessage" : "",\
			"syncingTo" : "172.31.34.245:27017",\
			"syncSourceHost" : "172.31.34.245:27017"\,\
			"syncSourceId" : 0,\
			"infoMessage" : "",\
			"configVersion" : 3\
		},\
		{\
			"_id" : 2,\
			"name" : "node3:27017",\
			"ip" : "172.31.17.138",\
			"health" : 1,\
			"state" : 2,\
			"stateStr" : "SECONDARY",\
			"uptime" : 77868,\
			"optime" : {\
				"ts" : Timestamp(1572448687, 1),\
				"t" : NumberLong(1)\
			},\
			"optimeDurable" : {\
				"ts" : Timestamp(1572448687, 1),\
				"t" : NumberLong(1)\
			},\
			"optimeDate" : ISODate("2019-10-30T15:18:07Z"),\
			"optimeDurableDate" : ISODate("2019-10-30T15:18:07Z"),\
			"lastHeartbeat" : ISODate("2019-10-30T15:18:15.879Z"),\
			"lastHeartbeatRecv" : ISODate("2019-10-30T15:18:15.878Z"),\
			"pingMs" : NumberLong(0),\
			"lastHeartbeatMessage" : "",\
			"syncingTo" : "172.31.34.245:27017",\
			"syncSourceHost" : "172.31.34.245:27017",\
			"syncSourceId" : 0,\
			"infoMessage" : "",\
			"configVersion" : 3\
		}\
	],\
	"ok" : 1,\
	"$clusterTime" : {\
		"clusterTime" : Timestamp(1572448687, 1),\
		"signature" : {\
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),\
			"keyId" : NumberLong(0)\
		}\
	},\
	"operationTime" : Timestamp(1572448687, 1)\
}\


### Output of 'rs.config' before shutdown of primary mongodb instance: 


rs0:PRIMARY> rs.config()\
{\
	"_id" : "rs0",\
	"version" : 3,\
	"protocolVersion" : NumberLong(1),\
	"writeConcernMajorityJournalDefault" : true,\
	"members" : [\
		{\
			"_id" : 0,\
			"host" : "172.31.34.245:27017",\
			"arbiterOnly" : false,\
			"buildIndexes" : true,\
			"hidden" : false,\
			"priority" : 1,\
			"tags" : {\
				\
			},\
			"slaveDelay" : NumberLong(0),\
			"votes" : 1\
		},\
		{\
			"_id" : 1,\
			"host" : "node2:27017",\
			"arbiterOnly" : false,\
			"buildIndexes" : true,\
			"hidden" : false,\
			"priority" : 1,\
			"tags" : {\
				\
			},\
			"slaveDelay" : NumberLong(0),\
			"votes" : 1\
		},\
		{\
			"_id" : 2,\
			"host" : "node3:27017",\
			"arbiterOnly" : false,\
			"buildIndexes" : true,\
			"hidden" : false,\
			"priority" : 1,\
			"tags" : {\
				\
			},\
			"slaveDelay" : NumberLong(0),\
			"votes" : 1\
		}\
	],\
	"settings" : {\
		"chainingAllowed" : true,\
		"heartbeatIntervalMillis" : 2000,\
		"heartbeatTimeoutSecs" : 10,\
		"electionTimeoutMillis" : 10000,\
		"catchUpTimeoutMillis" : -1,\
		"catchUpTakeoverDelayMillis" : 30000,\
		"getLastErrorModes" : {\
			\
		},\
		"getLastErrorDefaults" : {\
			"w" : 1,\
			"wtimeout" : 0\
		},\
		"replicaSetId" : ObjectId("5db87884e32245ac105cdbf8")\
	}\
}


### my brand new stylish chat web app before shutdown

![screenshot](https://github.com/thedownhill/Distributed-Systems/blob/master/lab9/screen_before.png)

### output of 'rs.status()' after shutdown (now node with id=0 is unavailable and node with id=1 is PRIMARY):

rs0:PRIMARY> rs.status()\
{\
	"set" : "rs0",\
	"date" : ISODate("2019-10-30T16:16:32.551Z"),\
	"myState" : 1,\
	"term" : NumberLong(2),\
	"syncingTo" : "",\
	"syncSourceHost" : "",\
	"syncSourceId" : -1,\
	"heartbeatIntervalMillis" : NumberLong(2000),\
	"majorityVoteCount" : 2,\
	"writeMajorityCount" : 2,\
	"optimes" : {\
		"lastCommittedOpTime" : {\
			"ts" : Timestamp(1572452191, 1),\
			"t" : NumberLong(2)\
		},\
		"lastCommittedWallTime" : ISODate("2019-10-30T16:16:31.908Z"),\
		"readConcernMajorityOpTime" : {\
			"ts" : Timestamp(1572452191, 1),\
			"t" : NumberLong(2)\
		},\
		"readConcernMajorityWallTime" : ISODate("2019-10-30T16:16:31.908Z"),\
		"appliedOpTime" : {\
			"ts" : Timestamp(1572452191, 1),\
			"t" : NumberLong(2)\
		},\
		"durableOpTime" : {\
			"ts" : Timestamp(1572452191, 1),\
			"t" : NumberLong(2)\
		},\
		"lastAppliedWallTime" : ISODate("2019-10-30T16:16:31.908Z"),\
		"lastDurableWallTime" : ISODate("2019-10-30T16:16:31.908Z")\
	},\
	"lastStableRecoveryTimestamp" : Timestamp(1572452151, 1),\
	"lastStableCheckpointTimestamp" : Timestamp(1572452151, 1),\
	"electionCandidateMetrics" : {\
		"lastElectionReason" : "stepUpRequestSkipDryRun",\
		"lastElectionDate" : ISODate("2019-10-30T16:14:31.011Z"),\
		"termAtElection" : NumberLong(2),\
		"lastCommittedOpTimeAtElection" : {\
			"ts" : Timestamp(1572452067, 1),\
			"t" : NumberLong(1)\
		},\
		"lastSeenOpTimeAtElection" : {\
			"ts" : Timestamp(1572452067, 1),\
			"t" : NumberLong(1)\
		},\
		"numVotesNeeded" : 2,\
		"priorityAtElection" : 1,\
		"electionTimeoutMillis" : NumberLong(10000),\
		"priorPrimaryMemberId" : 0,\
		"numCatchUpOps" : NumberLong(27017),\
		"newTermStartDate" : ISODate("2019-10-30T16:14:31.904Z"),\
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-30T16:14:33.162Z")\
	},\
	"members" : [\
		{\
			"_id" : 0,\
			"name" : "172.31.34.245:27017",\
			"ip" : "172.31.34.245",\
			"health" : 0,\
			"state" : 8,\
			"stateStr" : "(not reachable/healthy)",\
			"uptime" : 0,\
			"optime" : {\
				"ts" : Timestamp(0, 0),\
				"t" : NumberLong(-1)\
			},\
			"optimeDurable" : {\
				"ts" : Timestamp(0, 0),\
				"t" : NumberLong(-1)\
			},\
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),\
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),\
			"lastHeartbeat" : ISODate("2019-10-30T16:16:24.712Z"),\
			"lastHeartbeatRecv" : ISODate("2019-10-30T16:14:30.679Z"),\
			"pingMs" : NumberLong(0),\
			"lastHeartbeatMessage" : "Error connecting to 172.31.34.245:27017 :: caused by :: No route to host",\
			"syncingTo" : "",\
			"syncSourceHost" : "",\
			"syncSourceId" : -1,\
			"infoMessage" : "",\
			"configVersion" : -1\
		},\
		{\
			"_id" : 1,\
			"name" : "node2:27017",\
			"ip" : "172.31.34.52",\
			"health" : 1,\
			"state" : 1,\
			"stateStr" : "PRIMARY",\
			"uptime" : 83366,\
			"optime" : {\
				"ts" : Timestamp(1572452191, 1),\
				"t" : NumberLong(2)\
			},\
			"optimeDate" : ISODate("2019-10-30T16:16:31Z"),\
			"syncingTo" : "",\
			"syncSourceHost" : "",\
			"syncSourceId" : -1,\
			"infoMessage" : "",\
			"electionTime" : Timestamp(1572452071, 1),\
			"electionDate" : ISODate("2019-10-30T16:14:31Z"),\
			"configVersion" : 3,\
			"self" : true,\
			"lastHeartbeatMessage" : ""\
		},\
		{\
			"_id" : 2,\
			"name" : "node3:27017",\
			"ip" : "172.31.17.138",\
			"health" : 1,\
			"state" : 2,\
			"stateStr" : "SECONDARY",\
			"uptime" : 81365,\
			"optime" : {\
				"ts" : Timestamp(1572452181, 1),\
				"t" : NumberLong(2)\
			},\
			"optimeDurable" : {\
				"ts" : Timestamp(1572452181, 1),\
				"t" : NumberLong(2)\
			},\
			"optimeDate" : ISODate("2019-10-30T16:16:21Z"),\
			"optimeDurableDate" : ISODate("2019-10-30T16:16:21Z"),\
			"lastHeartbeat" : ISODate("2019-10-30T16:16:31.074Z"),\
			"lastHeartbeatRecv" : ISODate("2019-10-30T16:16:31.217Z"),\
			"pingMs" : NumberLong(0),\
			"lastHeartbeatMessage" : "",\
			"syncingTo" : "node2:27017",\
			"syncSourceHost" : "node2:27017",\
			"syncSourceId" : 1,\
			"infoMessage" : "",\
			"configVersion" : 3\
		}\
	],\
	"ok" : 1,\
	"$clusterTime" : {\
		"clusterTime" : Timestamp(1572452191, 1),\
		"signature" : {\
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),\
			"keyId" : NumberLong(0)\
		}\
	},\
	"operationTime" : Timestamp(1572452191, 1)\
}

### output of 'rs.config()' after shutdown: 


rs0:PRIMARY> rs.config()\
{\
	"_id" : "rs0",\
	"version" : 3,\
	"protocolVersion" : NumberLong(1),\
	"writeConcernMajorityJournalDefault" : true,\
	"members" : [\
		{\
			"_id" : 0,\
			"host" : "172.31.34.245:27017",\
			"arbiterOnly" : false,\
			"buildIndexes" : true,\
			"hidden" : false,\
			"priority" : 1,\
			"tags" : {\
				\
			},\
			"slaveDelay" : NumberLong(0),\
			"votes" : 1\
		},\
		{\
			"_id" : 1,\
			"host" : "node2:27017",\
			"arbiterOnly" : false,\
			"buildIndexes" : true,\
			"hidden" : false,\
			"priority" : 1,\
			"tags" : {\
				\
			},\
			"slaveDelay" : NumberLong(0),\
			"votes" : 1\
		},\
		{\
			"_id" : 2,\
			"host" : "node3:27017",\
			"arbiterOnly" : false,\
			"buildIndexes" : true,\
			"hidden" : false,\
			"priority" : 1,\
			"tags" : {\
				\
			},\
			"slaveDelay" : NumberLong(0),\
			"votes" : 1\
		}\
	],\
	"settings" : {\
		"chainingAllowed" : true,\
		"heartbeatIntervalMillis" : 2000,\
		"heartbeatTimeoutSecs" : 10,\
		"electionTimeoutMillis" : 10000,\
		"catchUpTimeoutMillis" : -1,\
		"catchUpTakeoverDelayMillis" : 30000,\
		"getLastErrorModes" : {\
			\
		},\
		"getLastErrorDefaults" : {\
			"w" : 1,\
			"wtimeout" : 0\
		},\
		"replicaSetId" : ObjectId("5db87884e32245ac105cdbf8")\
	}\
}

### my brand new stylish web app after shutdown (nothing changed; still work):

![screenshot](https://github.com/thedownhill/Distributed-Systems/blob/master/lab9/screen_after.png)


