# SyncBackupUtil
## Features

- 디렉토리의 싱크를 통한 백업을 하기 위한 유틸리티.
- 환경 설정은 config.yaml을 통해서 진행.
- 주말에는 알림이 전송되지 않는다.

## Configuration
purge: 원본 폴더에서 삭제된 파일을 백업 폴더에서도 삭제할지 여부
```sh
true/false
```

source : 원본 폴더
```sh
path : ex) c:\sources\workspace\project1
```

target : 백업 폴더
```sh
path : ex) d:\backups\workspace\project1
```