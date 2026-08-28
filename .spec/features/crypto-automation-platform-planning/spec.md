# Spec: Crypto automation platform planning

> feature: crypto-automation-platform-planning
> status: pronta

## Contexto

Como responsável de produto e segurança, preciso de uma baseline SDD verificável antes de permitir qualquer implementação financeira, para que futuros agentes recebam contratos, gates e uma fila sem precisar inventar autoridade sobre fundos.

## Histórias

### US-001 — Baseline documental canônica

Como responsável de arquitetura, quero todas as especificações, ADRs, contratos e diagramas canônicos no repositório correto, para que o planejamento possa ser revisado sem depender de arquivos externos.

#### AC-001 — Inventário canônico existe

- **Dado** o repositório `E:\BOT`
- **Quando** o validador de planejamento é executado
- **Então** todos os caminhos obrigatórios existem e nenhum está ausente.

#### AC-002 — Decisões estão explícitas

- **Dado** a baseline canônica
- **Quando** os ADRs são inventariados
- **Então** existem 15 ADRs e eles preservam autoridade determinística, ledger singular, modularidade e gates de evidência.

#### AC-003 — Diagramas e contratos são entregáveis verificáveis

- **Dado** a arquitetura planejada
- **Quando** os arquivos Mermaid e contratos são lidos
- **Então** existem pelo menos 11 diagramas e 10 contratos versionáveis para os limites de maior risco.

### US-002 — Fila executável e rastreabilidade

Como futuro implementador, quero cartões de PR pequenos com dependências formais e rastreabilidade de requisitos, para que mudanças possam ser executadas e auditadas sem ciclos ou trabalho oculto.

#### AC-004 — Cartões contêm contrato completo

- **Dado** a fila de implementação
- **Quando** cada cartão é validado
- **Então** os 133 cartões contêm objetivo, escopo, arquivos, dependências, implementação, testes, aceite, segurança, observabilidade, rollback e definição de pronto.

#### AC-005 — DAG não contém ciclo

- **Dado** as dependências da fila
- **Quando** a validação topológica é executada
- **Então** a DAG é acíclica e possui caminho crítico declarado.

#### AC-006 — Requisitos do mandato têm destino

- **Dado** os 68 grupos normalizados do mandato do usuário
- **Quando** a matriz de rastreabilidade é validada
- **Então** cada grupo aponta para uma especificação, uma família de teste futuro e cartões da fila.

### US-003 — Segurança de escopo

Como responsável por capital e compliance, quero que a baseline prove suas próprias limitações, para que documentação não seja confundida com autorização financeira.

#### AC-007 — Mainnet permanece bloqueada

- **Dado** a matriz de prontidão
- **Quando** o planejamento é verificado
- **Então** `MAINNET = BLOCKED` e nenhum status de planejamento é promovido a PASS operacional.

#### AC-008 — Nenhum runtime financeiro foi criado

- **Dado** o repositório de planejamento
- **Quando** as raízes de produto são verificadas
- **Então** não existem código de runtime, integração de provedor, signing, trade, wallet financiada ou endpoint financeiro.

### US-004 — Evidência honesta

Como auditor de planejamento, quero que a evidência local seja classificada, para que URL reachability e documentos não sejam apresentados como capacidade, aprovação ou produção.

#### AC-009 — Relatório limita seu próprio escopo

- **Dado** o relatório de integridade
- **Quando** ele é lido
- **Então** declara PASS apenas para topologia documental e mantém explicitamente `MAINNET = BLOCKED`.

#### AC-010 — Artefatos não contêm segredo

- **Dado** a baseline documental e seus testes
- **Quando** padrões de tokens e chaves são verificados
- **Então** nenhum segredo é encontrado.

### US-005 — Página de progresso não financeira

Como interessado no projeto, quero uma página estática `/develop`, para acompanhar a baseline de planejamento sem confundi-la com o produto financeiro.

#### AC-011 — Página develop é estática e declara o bloqueio

- **Dado** o artefato de status e a configuração Vercel
- **Quando** os arquivos são verificados localmente
- **Então** existe `develop/index.html`, informa `PLANNING BASELINE`, `133`, `68` e `MAINNET BLOCKED`, e não inclui formulários, scripts externos, credenciais ou integração financeira.

## Fora de escopo

- Código de produto, schemas de banco executáveis, migrations, contas, segredos, integração Mercado Pago, exchange, wallet, KMS, IA, signing, Pix, trade, testnet, mainnet, deploy financeiro ou conclusão jurídica.

## Suposições

| ID | Suposição | Status | Resolução |
|---|---|---|---|
| ASM-001 | A fila de 133 cartões tem granularidade suficiente para a primeira execução e só será alterada por evidência de responsabilidade/prova distinta. | confirmada | Validada por contrato de cartões e DAG; não é meta numérica. |
| ASM-002 | Os 68 grupos normalizados cobrem todos os tópicos do mandato longo do usuário. | confirmada | Matriz `TRACEABILITY_MATRIX.md` é a fonte auditável. |

## Perguntas em aberto

| ID | Pergunta | Status | Resposta |
|---|---|---|---|
| Q-001 | Qual entidade, jurisdição e classificação legal permite qualquer capital real? | aberta | Ver `.planning/master/OPEN_QUESTIONS.md`. |
| Q-002 | Que capacidades de provedor, custódia e assinatura podem ser realmente habilitadas? | aberta | Ver `.planning/master/OPEN_QUESTIONS.md`. |
| Q-003 | Qual linguagem de kernel satisfaz o spike de evidência? | aberta | ADR-001 permanece Proposed. |
