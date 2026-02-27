FROM postgres:15-alpine

# 设置默认环境变量
ENV POSTGRES_DB=judgement_db
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# (可选) 将初始化 SQL 脚本拷贝到容器中，容器启动时会自动执行这些脚本
# COPY ./init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
